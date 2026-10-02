"""Resolução segura de mídias incorporadas e conversão de legendas."""

from __future__ import annotations

import json
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, unquote, urljoin, urlparse

import httpx
from bs4 import BeautifulSoup

from canvas_crawler.canvas import CanvasClient
from canvas_crawler.exceptions import CanvasApiError, CanvasCrawlerError
from canvas_crawler.transcription import FasterWhisperTranscriber


@dataclass(frozen=True, slots=True)
class MediaResult:
    status: str
    transcript: Path | None = None
    reason: str | None = None
    provider: str = "unknown"


def _seconds(value: str) -> float:
    value = value.strip().replace(",", ".")
    pieces = value.split(":")
    try:
        if len(pieces) == 3:
            hours, minutes, seconds = pieces
        else:
            hours, minutes, seconds = "0", pieces[0], pieces[1]
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    except (ValueError, IndexError) as error:
        raise CanvasCrawlerError(f"Timestamp de legenda inválido: {value}") from error


def save_caption_transcript(content: str, output: Path, *, title: str) -> Path:
    """Converte WebVTT/SRT em Markdown e JSON pesquisáveis."""

    normalized = content.replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n{2,}", normalized.strip())
    segments: list[dict[str, object]] = []
    timing = re.compile(
        r"(?P<start>\d{1,2}:\d{2}(?::\d{2})?[,.]\d+)\s*-->\s*"
        r"(?P<end>\d{1,2}:\d{2}(?::\d{2})?[,.]\d+)"
    )
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        match = next((timing.search(line) for line in lines if timing.search(line)), None)
        if match is None:
            continue
        time_index = next(index for index, line in enumerate(lines) if timing.search(line))
        text = " ".join(lines[time_index + 1 :])
        text = re.sub(r"<[^>]+>", "", text).strip()
        if text:
            segments.append(
                {
                    "start": _seconds(match.group("start")),
                    "end": _seconds(match.group("end")),
                    "text": text,
                }
            )
    if not segments:
        raise CanvasCrawlerError("A legenda não contém segmentos reconhecíveis.")

    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {title}", "", "- Origem: legenda disponibilizada pelo provedor", "", "## Transcrição", ""]
    for segment in segments:
        total = int(float(segment["start"]))
        hours, remainder = divmod(total, 3600)
        minutes, seconds = divmod(remainder, 60)
        lines.extend([f"**[{hours:02d}:{minutes:02d}:{seconds:02d}]** {segment['text']}", ""])
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    output.with_suffix(".json").write_text(
        json.dumps({"title": title, "source": "captions", "segments": segments}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


class CanvasStudioResolver:
    """Usa o lançamento LTI oficial sem enviar o token Canvas ao Studio."""

    def __init__(self, canvas: CanvasClient, *, timeout: float) -> None:
        self._canvas = canvas
        self._timeout = timeout

    @staticmethod
    def supports(url: str) -> bool:
        parsed = urlparse(url)
        target = parse_qs(parsed.query).get("url", [""])[0]
        return "/external_tools/" in parsed.path and "instructuremedia.com" in target

    def process(
        self,
        *,
        course_id: int,
        iframe_url: str,
        title: str,
        output: Path,
        temp_root: Path,
        transcriber: FasterWhisperTranscriber,
    ) -> MediaResult:
        if output.exists() and output.with_suffix(".json").exists():
            return MediaResult("existing", output, provider="canvas-studio")

        parsed_iframe = urlparse(iframe_url)
        target = unquote(parse_qs(parsed_iframe.query).get("url", [""])[0])
        if not target:
            return MediaResult("pending", reason="Embed Studio sem URL LTI.", provider="canvas-studio")

        try:
            launch_url = self._canvas.get_sessionless_launch_url(course_id, target)
        except CanvasCrawlerError:
            return MediaResult(
                "pending",
                reason="Canvas não autorizou o lançamento LTI desta mídia.",
                provider="canvas-studio",
            )
        with httpx.Client(
            follow_redirects=True,
            timeout=self._timeout,
            headers={"User-Agent": "CanvasCrawler/0.1"},
        ) as session:
            try:
                canvas_launch = session.get(launch_url)
                canvas_launch.raise_for_status()
                form = BeautifulSoup(canvas_launch.text, "html.parser").find("form", id="tool_form")
                if form is None:
                    return MediaResult("pending", reason="Canvas não gerou o formulário LTI.", provider="canvas-studio")
                action = urljoin(str(canvas_launch.url), str(form.get("action") or ""))
                self._validate_studio_url(action)
                payload = {
                    str(field.get("name")): str(field.get("value") or "")
                    for field in form.find_all("input")
                    if field.get("name")
                }
                response = session.post(action, data=payload, follow_redirects=False)
                if not response.is_redirect:
                    response.raise_for_status()
                    return MediaResult(
                        "pending",
                        reason="Canvas Studio não redirecionou o lançamento LTI.",
                        provider="canvas-studio",
                    )
                redirect = response.headers.get("location")
                if not redirect:
                    return MediaResult(
                        "pending",
                        reason="Canvas Studio redirecionou sem informar o destino.",
                        provider="canvas-studio",
                    )
                location = urljoin(str(response.url), redirect)
                studio_url = urlparse(location)
                self._validate_studio_url(location)
                lti_params = parse_qs(studio_url.query).get("lti_params", [""])[0]
                embed_id = studio_url.path.rsplit("/", maxsplit=1)[-1]
                if not lti_params or not embed_id:
                    return MediaResult("pending", reason="Lançamento Studio incompleto.", provider="canvas-studio")

                decoded = session.get(
                    f"{studio_url.scheme}://{studio_url.netloc}/api/lti/launch_params",
                    params={"lti_params": lti_params},
                    headers={"Accept": "application/json"},
                )
                decoded.raise_for_status()
                launch = decoded.json()
                studio_headers = self._studio_headers(launch, lti_params)
                base = f"{studio_url.scheme}://{studio_url.netloc}"
                perspective_response = session.get(
                    f"{base}/api/media_management/media/{embed_id}/lti_perspective",
                    params={"lti_params": lti_params},
                    headers=studio_headers,
                )
                perspective_response.raise_for_status()
                perspective_id = perspective_response.json()["perspective_id"]
                metadata = session.get(
                    f"{base}/api/media_management/perspectives/{perspective_id}",
                    headers=studio_headers,
                )
                metadata.raise_for_status()
                media = metadata.json()["perspective"]["media"]

                if launch.get("embed_transcript_downloadable"):
                    captions = media.get("captions") or []
                    if captions:
                        caption = self._choose_caption(captions)
                        caption_response = session.get(str(caption["url"]), headers=studio_headers)
                        caption_response.raise_for_status()
                        save_caption_transcript(caption_response.text, output, title=title)
                        return MediaResult("transcribed", output, provider="canvas-studio-caption")

                if not launch.get("embed_downloadable"):
                    return MediaResult(
                        "blocked",
                        reason="O proprietário desabilitou o download da mídia e da transcrição.",
                        provider="canvas-studio",
                    )
                source = self._choose_source(media.get("sources") or [])
                if source is None:
                    return MediaResult("pending", reason="Studio não informou fonte baixável.", provider="canvas-studio")
                temp_root.mkdir(parents=True, exist_ok=True)
                with tempfile.NamedTemporaryFile(dir=temp_root, suffix=".media", delete=False) as temporary:
                    media_path = Path(temporary.name)
                try:
                    with session.stream("GET", source, headers=studio_headers) as download:
                        download.raise_for_status()
                        with media_path.open("wb") as file:
                            for chunk in download.iter_bytes():
                                file.write(chunk)
                    transcriber.transcribe(media_path, output, title=title)
                    return MediaResult("transcribed", output, provider="canvas-studio-media")
                finally:
                    media_path.unlink(missing_ok=True)
            except httpx.HTTPStatusError as error:
                return MediaResult(
                    "pending",
                    reason=f"Canvas Studio respondeu HTTP {error.response.status_code}.",
                    provider="canvas-studio",
                )
            except httpx.HTTPError:
                return MediaResult(
                    "pending",
                    reason="Falha de comunicação com o Canvas Studio.",
                    provider="canvas-studio",
                )
            except (CanvasCrawlerError, KeyError, TypeError, ValueError):
                return MediaResult(
                    "pending",
                    reason="Canvas Studio retornou uma resposta incompleta ou inesperada.",
                    provider="canvas-studio",
                )

    @staticmethod
    def _validate_studio_url(url: str) -> None:
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.hostname or not parsed.hostname.endswith(".instructuremedia.com"):
            raise CanvasApiError("O lançamento LTI apontou para um domínio inesperado.")

    @staticmethod
    def _studio_headers(launch: dict[str, object], lti_params: str) -> dict[str, str]:
        session = launch.get("session")
        if not isinstance(session, dict) or not isinstance(session.get("user"), dict):
            raise CanvasApiError("Studio não retornou uma sessão válida.")
        user_id = session["user"].get("id")
        token = session.get("token")
        if not user_id or not token:
            raise CanvasApiError("Studio não retornou credenciais temporárias.")
        return {
            "Accept": "application/json",
            "X-Lti-Params": lti_params,
            "Authorization": f'Bearer user_id="{user_id}", token="{token}"',
        }

    @staticmethod
    def _choose_caption(captions: list[dict[str, object]]) -> dict[str, object]:
        return next((item for item in captions if str(item.get("srclang", "")).startswith("pt")), captions[0])

    @staticmethod
    def _choose_source(sources: list[dict[str, object]]) -> str | None:
        for source in sources:
            value = source.get("download_url") or source.get("url")
            if value:
                return str(value)
        return None
