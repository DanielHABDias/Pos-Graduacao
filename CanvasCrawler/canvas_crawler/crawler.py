"""Orquestra a coleta de uma disciplina e a criação do acervo portátil."""

from __future__ import annotations

import mimetypes
import re
import tempfile
from hashlib import sha256
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify

from canvas_crawler.canvas import CanvasClient
from canvas_crawler.config import Settings
from canvas_crawler.exceptions import CanvasCrawlerError
from canvas_crawler.media import CanvasStudioResolver, save_caption_transcript
from canvas_crawler.models import Course, FileAsset, Module, ModuleItem, Page, Program
from canvas_crawler.storage import CourseWorkspace, Manifest, ModuleWorkspace, NamingPolicy
from canvas_crawler.transcription import FasterWhisperTranscriber


@dataclass(slots=True)
class CrawlResult:
    course_root: Path
    pages: int = 0
    files: int = 0
    images: int = 0
    transcripts: int = 0
    existing: int = 0
    skipped: int = 0
    failures: int = 0
    media_pending: int = 0
    media_blocked: int = 0


class CourseCrawler:
    """Coleta uma disciplina sem executar atividades ou preservar vídeos."""

    _SKIPPED_TYPES = {"Assignment", "Quiz", "Discussion"}
    _FILE_ID_PATTERN = re.compile(r"/files/(?:file_id:)?(\d+)")
    _MEDIA_ATTACHMENT_PATTERN = re.compile(r"/media_attachments_iframe/(\d+)")

    def __init__(self, client: CanvasClient, settings: Settings) -> None:
        self._client = client
        self._settings = settings
        self._transcriber = FasterWhisperTranscriber(
            model_name=settings.whisper_model,
            language=settings.whisper_language,
            device=settings.whisper_device,
        )
        self._downloaded_files: dict[tuple[int, int], Path] = {}
        self._claimed_paths: dict[Path, int] = {}
        self._studio = CanvasStudioResolver(client, timeout=settings.timeout_seconds)
        self._media_attachments: dict[int, dict[str, object]] | None = None

    def crawl(self, program: Program, course: Course) -> CrawlResult:
        self._downloaded_files.clear()
        self._claimed_paths.clear()
        self._media_attachments = None
        workspace = CourseWorkspace.create(self._settings.output_dir, program, course)
        manifest = Manifest(
            workspace.metadata_dir / "manifest.json", program=program, course=course
        )
        result = CrawlResult(course_root=workspace.course_root)
        modules = self._client.list_modules(course.id)
        module_links: list[str] = []

        for module in modules:
            module_workspace = ModuleWorkspace.create(workspace.course_root, module)
            module_links.append(f"- [{module.name}]({module_workspace.root.name}/README.md)")
            item_lines = [f"# {module.name}", "", f"Itens informados pelo Canvas: {module.items_count}", ""]

            for item in self._client.list_module_items(course.id, module.id):
                try:
                    line = self._process_item(
                        course,
                        module,
                        item,
                        module_workspace,
                        manifest,
                        result,
                    )
                except (CanvasCrawlerError, OSError, RuntimeError, ValueError) as error:
                    result.failures += 1
                    line = f"- ⚠️ {item.title} — falha: {error}"
                    manifest.record(self._entry(module, item, "error", error=str(error)))
                item_lines.append(line)

            (module_workspace.root / "README.md").write_text(
                "\n".join(item_lines).rstrip() + "\n", encoding="utf-8"
            )

        course_readme = [
            f"# {course.name}",
            "",
            f"- Formação: {program.name}",
            f"- ID no Canvas: {course.id}",
            f"- Código: {course.course_code or '-'}",
            "",
            "## Módulos",
            "",
            *module_links,
            "",
            "## Coleta",
            "",
            "Este índice foi gerado pelo CanvasCrawler. Atividades, provas e discussões não são coletadas.",
        ]
        (workspace.course_root / "README.md").write_text(
            "\n".join(course_readme).rstrip() + "\n", encoding="utf-8"
        )
        self._write_formation_index(workspace.formation_root, program)
        return result

    def _process_item(
        self,
        course: Course,
        module: Module,
        item: ModuleItem,
        workspace: ModuleWorkspace,
        manifest: Manifest,
        result: CrawlResult,
    ) -> str:
        if item.type in self._SKIPPED_TYPES:
            result.skipped += 1
            manifest.record(self._entry(module, item, "skipped", reason="avaliativo"))
            return f"- ⏭️ {item.title} — {item.type} ignorado"
        if item.type == "SubHeader":
            manifest.record(self._entry(module, item, "heading"))
            return f"- **{item.title}**"
        if item.type == "Page" and item.page_url:
            page = self._client.get_page(course.id, item.page_url)
            markdown_path = self._save_page(course, module, item, page, workspace, manifest, result)
            return f"- [{item.title}](paginas/{markdown_path.name}) — página"
        if item.type == "File" and item.content_id is not None:
            asset = self._client.get_file(item.content_id)
            path, artifact = self._save_file(module, item, asset, workspace, manifest, result)
            relative = path.relative_to(workspace.root).as_posix()
            return f"- [{item.title}]({relative}) — {artifact}"
        if item.type in {"ExternalUrl", "ExternalTool"}:
            target = item.external_url or item.html_url or ""
            manifest.record(self._entry(module, item, "external-link", url=target))
            return f"- [{item.title}]({target}) — link externo"

        result.skipped += 1
        manifest.record(self._entry(module, item, "skipped", reason="tipo não suportado"))
        return f"- ⏭️ {item.title} — tipo {item.type} não suportado"

    def _save_page(
        self,
        course: Course,
        module: Module,
        item: ModuleItem,
        page: Page,
        workspace: ModuleWorkspace,
        manifest: Manifest,
        result: CrawlResult,
    ) -> Path:
        basename = NamingPolicy.numbered(item.position, page.title, fallback=f"Página {page.id}")
        if self._settings.keep_source_html:
            html_path = workspace.ensure(workspace.html) / f"{basename}.html"
            self._write_if_changed(html_path, page.body)

        soup = BeautifulSoup(page.body, "html.parser")
        self._localize_page_resources(course, module, item, soup, workspace, manifest, result)
        markdown = markdownify(str(soup), heading_style="ATX", bullets="-")
        source_url = f"{self._settings.base_url}/courses/{course.id}/pages/{page.url}"
        text = f"# {page.title}\n\n- Origem: [Canvas]({source_url})\n\n{markdown.strip()}\n"
        markdown_path = workspace.ensure(workspace.pages) / f"{basename}.md"
        self._write_if_changed(markdown_path, text)
        result.pages += 1
        manifest.record(
            self._entry(
                module,
                item,
                "page",
                path=str(markdown_path.relative_to(workspace.root)),
                canvas_page_id=page.id,
                updated_at=page.updated_at,
                sha256=NamingPolicy.sha256(markdown_path),
            )
        )
        return markdown_path

    def _localize_page_resources(
        self,
        course: Course,
        module: Module,
        item: ModuleItem,
        soup: BeautifulSoup,
        workspace: ModuleWorkspace,
        manifest: Manifest,
        result: CrawlResult,
    ) -> None:
        base_url = f"{self._settings.base_url}/courses/{course.id}/pages/"
        for index, image in enumerate(soup.find_all("img"), start=1):
            source = image.get("src")
            if not source or source.startswith("data:"):
                continue
            url = urljoin(base_url, source)
            file_id = self._file_id(image.get("data-api-endpoint") or url)
            try:
                if file_id is not None:
                    asset = self._client.get_file(file_id)
                    path, _ = self._save_file(
                        module, item, asset, workspace, manifest, result, force_image=True
                    )
                else:
                    title = image.get("alt") or image.get("title") or f"{item.title} imagem {index}"
                    path = self._download_direct_image(
                        url,
                        title,
                        index,
                        item.id * 10_000 + index,
                        workspace,
                        result,
                    )
                    manifest.record(
                        self._entry(
                            module,
                            item,
                            "embedded-image",
                            path=str(path.relative_to(workspace.root)),
                            url=url.split("?", maxsplit=1)[0],
                            size=path.stat().st_size,
                            sha256=NamingPolicy.sha256(path),
                        )
                    )
                image["src"] = f"../images/{path.name}"
            except (CanvasCrawlerError, OSError, RuntimeError, ValueError):
                continue

        for link in soup.find_all("a"):
            href = link.get("href")
            endpoint = link.get("data-api-endpoint")
            file_id = self._file_id(endpoint or href or "")
            if file_id is None:
                continue
            try:
                asset = self._client.get_file(file_id)
                path, _ = self._save_file(module, item, asset, workspace, manifest, result)
                link["href"] = f"../{path.parent.name}/{path.name}"
            except (CanvasCrawlerError, OSError, RuntimeError, ValueError):
                continue

        for media in soup.find_all(["video", "audio", "source"]):
            source = media.get("src")
            if not source:
                continue
            url = urljoin(base_url, source)
            try:
                transcript = self._transcribe_url(url, item.title, workspace, result)
                transcript_link = soup.new_tag(
                    "a", href=f"../transcricoes/{transcript.name}"
                )
                transcript_link.string = f"Transcrição: {item.title}"
                media.replace_with(transcript_link)
            except (CanvasCrawlerError, OSError, RuntimeError, ValueError):
                continue

        for index, frame in enumerate(soup.find_all("iframe"), start=1):
            source = frame.get("src")
            if not source:
                continue
            url = urljoin(base_url, source)
            attachment_match = self._MEDIA_ATTACHMENT_PATTERN.search(url)
            if attachment_match:
                self._process_native_media(
                    course,
                    module,
                    item,
                    workspace,
                    manifest,
                    result,
                    frame,
                    int(attachment_match.group(1)),
                    index,
                    url,
                )
                continue
            if not self._studio.supports(url):
                provider = self._external_media_provider(url)
                if provider:
                    result.media_pending += 1
                    manifest.record(
                        self._entry(
                            module,
                            item,
                            "media-pending",
                            provider=provider,
                            media_key=sha256(url.encode("utf-8")).hexdigest()[:16],
                            reason="Provedor externo sem download autorizado pela API configurada.",
                        )
                    )
                continue
            transcript_name = NamingPolicy.clean(
                f"{NamingPolicy.numbered(item.position, item.title, fallback='Página')} - Vídeo {index:02d}",
                fallback=f"video-{item.id}-{index}",
            )
            transcript = workspace.ensure(workspace.transcripts) / f"{transcript_name}.md"
            media_key = sha256(url.encode("utf-8")).hexdigest()[:16]
            outcome = self._studio.process(
                course_id=course.id,
                iframe_url=url,
                title=f"{item.title} — Vídeo {index}",
                output=transcript,
                temp_root=self._settings.output_dir / ".tmp",
                transcriber=self._transcriber,
            )
            if outcome.transcript is not None:
                if outcome.status == "transcribed":
                    result.transcripts += 1
                elif outcome.status == "existing":
                    result.existing += 1
                manifest.record(
                    self._entry(
                        module,
                        item,
                        "transcript",
                        path=str(outcome.transcript.relative_to(workspace.root)),
                        provider=outcome.provider,
                        media_key=media_key,
                        source_video_deleted=True,
                    )
                )
                manifest.remove_media_pending(
                    module_id=module.id, item_id=item.id, media_key=media_key
                )
                link = soup.new_tag("a", href=f"../transcricoes/{outcome.transcript.name}")
                link.string = f"Transcrição: {item.title} — Vídeo {index}"
                frame.replace_with(link)
            else:
                artifact = "media-blocked" if outcome.status == "blocked" else "media-pending"
                if outcome.status == "blocked":
                    result.media_blocked += 1
                else:
                    result.media_pending += 1
                manifest.remove_media_unavailable(
                    module_id=module.id, item_id=item.id, media_key=media_key
                )
                manifest.record(
                    self._entry(
                        module,
                        item,
                        artifact,
                        provider=outcome.provider,
                        media_key=media_key,
                        reason=outcome.reason,
                    )
                )

    def _save_file(
        self,
        module: Module,
        item: ModuleItem,
        asset: FileAsset,
        workspace: ModuleWorkspace,
        manifest: Manifest,
        result: CrawlResult,
        *,
        force_image: bool = False,
    ) -> tuple[Path, str]:
        cache_key = (module.id, asset.id)
        if cache_key in self._downloaded_files:
            path = self._downloaded_files[cache_key]
            return path, self._artifact_name(asset.content_type)

        if asset.content_type.startswith(("video/", "audio/")):
            transcript = self._transcribe_asset(asset, item.title, workspace, result)
            manifest.record(
                self._entry(
                    module,
                    item,
                    "transcript",
                    path=str(transcript.relative_to(workspace.root)),
                    canvas_file_id=asset.id,
                    source_video_deleted=True,
                )
            )
            self._downloaded_files[cache_key] = transcript
            return transcript, "transcrição"

        is_image = force_image or asset.content_type.startswith("image/")
        directory = workspace.ensure(workspace.images if is_image else workspace.documents)
        name = NamingPolicy.clean(
            asset.display_name or asset.filename,
            fallback=f"arquivo-canvas-{asset.id}",
        )
        destination = self._unique_path(directory / name, asset.id)
        if not destination.exists():
            self._client.download(self._asset_url(asset), destination)
            if is_image:
                result.images += 1
            else:
                result.files += 1
        else:
            result.existing += 1
        self._downloaded_files[cache_key] = destination
        manifest.record(
            self._entry(
                module,
                item,
                "image" if is_image else "document",
                path=str(destination.relative_to(workspace.root)),
                canvas_file_id=asset.id,
                content_type=asset.content_type,
                size=destination.stat().st_size,
                sha256=NamingPolicy.sha256(destination),
            )
        )
        return destination, "imagem" if is_image else "documento"

    def _download_direct_image(
        self,
        url: str,
        title: str,
        index: int,
        identifier: int,
        workspace: ModuleWorkspace,
        result: CrawlResult,
    ) -> Path:
        suffix = Path(unquote(urlparse(url).path)).suffix
        if not suffix or len(suffix) > 8:
            suffix = ".img"
        name = NamingPolicy.clean(title, fallback=f"imagem-{index}")
        destination = self._unique_path(
            workspace.ensure(workspace.images) / f"{name}{suffix}", identifier
        )
        if not destination.exists():
            content_type = self._client.download(url, destination)
            if destination.suffix == ".img":
                guessed = mimetypes.guess_extension(content_type) or ".img"
                renamed = destination.with_suffix(guessed)
                destination.replace(renamed)
                destination = renamed
            result.images += 1
        else:
            result.existing += 1
        return destination

    def _transcribe_asset(
        self, asset: FileAsset, title: str, workspace: ModuleWorkspace, result: CrawlResult
    ) -> Path:
        return self._transcribe_url(
            self._asset_url(asset),
            title,
            workspace,
            result,
            suffix=Path(asset.filename).suffix,
        )

    def _transcribe_url(
        self,
        url: str,
        title: str,
        workspace: ModuleWorkspace,
        result: CrawlResult,
        *,
        suffix: str = ".media",
    ) -> Path:
        if not self._settings.transcription_enabled:
            raise CanvasCrawlerError("Transcrição está desabilitada no .env.")
        safe_title = NamingPolicy.clean(title, fallback="transcricao")
        transcript = workspace.ensure(workspace.transcripts) / f"{safe_title}.md"
        if self._transcribe_to_path(url, transcript, title=title, suffix=suffix):
            result.transcripts += 1
        else:
            result.existing += 1
        return transcript

    def _transcribe_to_path(
        self,
        url: str,
        transcript: Path,
        *,
        title: str,
        suffix: str = ".media",
    ) -> bool:
        if not self._settings.transcription_enabled:
            raise CanvasCrawlerError("Transcrição está desabilitada no .env.")
        if transcript.exists() and transcript.with_suffix(".json").exists():
            return False
        temp_root = self._settings.output_dir / ".tmp"
        temp_root.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            dir=temp_root, suffix=suffix or ".media", delete=False
        ) as temporary:
            video_path = Path(temporary.name)
        try:
            self._client.download(url, video_path)
            self._transcriber.transcribe(video_path, transcript, title=title)
            return True
        finally:
            video_path.unlink(missing_ok=True)

    def _process_native_media(
        self,
        course: Course,
        module: Module,
        item: ModuleItem,
        workspace: ModuleWorkspace,
        manifest: Manifest,
        result: CrawlResult,
        frame: object,
        attachment_id: int,
        index: int,
        source_url: str,
    ) -> None:
        transcript_name = NamingPolicy.clean(
            f"{NamingPolicy.numbered(item.position, item.title, fallback='Página')} - Vídeo {index:02d}",
            fallback=f"video-{attachment_id}",
        )
        transcript = workspace.ensure(workspace.transcripts) / f"{transcript_name}.md"
        media_key = f"canvas-media-{attachment_id}"
        try:
            if transcript.exists() and transcript.with_suffix(".json").exists():
                outcome = "existing"
            else:
                tracks = self._client.list_media_tracks(attachment_id)
                track = next(
                    (
                        value
                        for value in tracks
                        if value.get("webvtt_content") or value.get("content")
                    ),
                    None,
                )
                if track:
                    save_caption_transcript(
                        str(track.get("webvtt_content") or track.get("content")),
                        transcript,
                        title=f"{item.title} — Vídeo {index}",
                    )
                    outcome = "transcribed"
                else:
                    attachment = self._native_attachment(course.id, attachment_id)
                    sources = attachment.get("media_sources") or []
                    media_url = next(
                        (
                            str(value.get("url"))
                            for value in sources
                            if isinstance(value, dict) and value.get("url")
                        ),
                        "",
                    )
                    if not media_url:
                        raise CanvasCrawlerError("Mídia nativa sem legenda ou fonte acessível.")
                    created = self._transcribe_to_path(
                        media_url,
                        transcript,
                        title=f"{item.title} — Vídeo {index}",
                    )
                    outcome = "transcribed" if created else "existing"
            if outcome == "transcribed":
                result.transcripts += 1
            else:
                result.existing += 1
            manifest.record(
                self._entry(
                    module,
                    item,
                    "transcript",
                    path=str(transcript.relative_to(workspace.root)),
                    provider="canvas-media",
                    media_key=media_key,
                    source_video_deleted=True,
                )
            )
            manifest.remove_media_pending(
                module_id=module.id, item_id=item.id, media_key=media_key
            )
            link = BeautifulSoup("", "html.parser").new_tag(
                "a", href=f"../transcricoes/{transcript.name}"
            )
            link.string = f"Transcrição: {item.title} — Vídeo {index}"
            frame.replace_with(link)  # type: ignore[attr-defined]
        except (CanvasCrawlerError, OSError, RuntimeError, ValueError) as error:
            result.media_pending += 1
            manifest.record(
                self._entry(
                    module,
                    item,
                    "media-pending",
                    provider="canvas-media",
                    media_key=media_key,
                    reason=str(error),
                    source_url=source_url.split("?", maxsplit=1)[0],
                )
            )

    def _native_attachment(self, course_id: int, attachment_id: int) -> dict[str, object]:
        if self._media_attachments is None:
            self._media_attachments = {
                int(value["id"]): value
                for value in self._client.list_media_attachments(course_id)
                if value.get("id") is not None
            }
        try:
            return self._media_attachments[attachment_id]
        except KeyError as error:
            raise CanvasCrawlerError(
                f"Anexo de mídia {attachment_id} não apareceu na API do curso."
            ) from error

    def _asset_url(self, asset: FileAsset) -> str:
        return asset.url or f"{self._settings.base_url}/files/{asset.id}/download"

    @staticmethod
    def _external_media_provider(url: str) -> str | None:
        host = (urlparse(url).hostname or "").casefold()
        if "youtube.com" in host or "youtu.be" in host:
            return "youtube"
        if "vimeo.com" in host:
            return "vimeo"
        return None

    @classmethod
    def _file_id(cls, value: str) -> int | None:
        match = cls._FILE_ID_PATTERN.search(value)
        return int(match.group(1)) if match else None

    @staticmethod
    def _artifact_name(content_type: str) -> str:
        if content_type.startswith("image/"):
            return "imagem"
        if content_type.startswith(("video/", "audio/")):
            return "transcrição"
        return "documento"

    def _unique_path(self, path: Path, identifier: int) -> Path:
        owner = self._claimed_paths.get(path)
        if owner is None or owner == identifier:
            self._claimed_paths[path] = identifier
            return path
        alternative = path.with_name(f"{path.stem}-canvas-{identifier}{path.suffix}")
        self._claimed_paths[alternative] = identifier
        return alternative

    @staticmethod
    def _write_if_changed(path: Path, content: str) -> None:
        if path.exists() and path.read_text(encoding="utf-8") == content:
            return
        path.write_text(content, encoding="utf-8")

    @staticmethod
    def _entry(
        module: Module,
        item: ModuleItem,
        artifact: str,
        **extra: object,
    ) -> dict[str, object]:
        return {
            "module_id": module.id,
            "module_name": module.name,
            "item_id": item.id,
            "item_title": item.title,
            "item_type": item.type,
            "artifact": artifact,
            **extra,
        }

    @staticmethod
    def _write_formation_index(root: Path, program: Program) -> None:
        disciplines = sorted(
            (directory for directory in root.iterdir() if directory.is_dir()),
            key=lambda path: path.name.casefold(),
        )
        lines = [f"# {program.name}", "", "## Disciplinas", ""]
        lines.extend(f"- [{path.name}]({path.name}/README.md)" for path in disciplines)
        (root / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
