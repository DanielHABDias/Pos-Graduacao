"""Transcrição local de vídeos, sem preservar o arquivo de mídia."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from canvas_crawler.exceptions import ConfigurationError


def _timestamp(seconds: float) -> str:
    total = max(0, int(seconds))
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


class FasterWhisperTranscriber:
    """Carrega o modelo somente quando o primeiro vídeo for encontrado."""

    def __init__(self, *, model_name: str, language: str, device: str) -> None:
        self._model_name = model_name
        self._language = language
        self._device = device
        self._model: Any = None

    def transcribe(self, video: Path, output_markdown: Path, *, title: str) -> Path:
        model = self._get_model()
        segments_iterator, info = model.transcribe(
            str(video),
            language=self._language,
            vad_filter=True,
            beam_size=5,
        )
        segments = [
            {"start": segment.start, "end": segment.end, "text": segment.text.strip()}
            for segment in segments_iterator
            if segment.text.strip()
        ]

        output_markdown.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            f"# {title}",
            "",
            f"- Idioma detectado: {info.language}",
            f"- Modelo: {self._model_name}",
            "",
            "## Transcrição",
            "",
        ]
        for segment in segments:
            lines.append(f"**[{_timestamp(segment['start'])}]** {segment['text']}")
            lines.append("")
        output_markdown.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

        output_markdown.with_suffix(".json").write_text(
            json.dumps(
                {
                    "title": title,
                    "language": info.language,
                    "language_probability": info.language_probability,
                    "model": self._model_name,
                    "segments": segments,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return output_markdown

    def _get_model(self) -> Any:
        if self._model is not None:
            return self._model
        try:
            from faster_whisper import WhisperModel
        except ImportError as error:
            raise ConfigurationError(
                "A transcrição requer faster-whisper. Execute ./canvas.sh preparar."
            ) from error

        self._model = WhisperModel(
            self._model_name,
            device=self._device,
            compute_type="int8",
        )
        return self._model
