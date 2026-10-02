"""Configuração da aplicação carregada do ambiente e do arquivo .env."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from canvas_crawler.exceptions import ConfigurationError


@dataclass(frozen=True, slots=True)
class Settings:
    """Configurações necessárias para acessar a API do Canvas."""

    base_url: str
    access_token: str
    per_page: int = 100
    timeout_seconds: float = 60.0
    output_dir: Path = Path("acervo")
    keep_source_html: bool = True
    transcription_enabled: bool = True
    whisper_model: str = "medium"
    whisper_language: str = "pt"
    whisper_device: str = "auto"

    @classmethod
    def from_env(cls, env_file: str | Path = ".env") -> Settings:
        """Cria as configurações sem sobrescrever variáveis já exportadas."""

        load_dotenv(dotenv_path=env_file, override=False)

        base_url = os.getenv("CANVAS_BASE_URL", "").strip().rstrip("/")
        access_token = os.getenv("CANVAS_ACCESS_TOKEN", "").strip()

        if not base_url:
            raise ConfigurationError("CANVAS_BASE_URL não foi configurada.")
        if not base_url.startswith("https://"):
            raise ConfigurationError("CANVAS_BASE_URL deve usar HTTPS.")
        if not access_token:
            raise ConfigurationError("CANVAS_ACCESS_TOKEN não foi configurado.")

        per_page = cls._read_int("CANVAS_PER_PAGE", default=100, minimum=1, maximum=100)
        timeout = cls._read_float(
            "CANVAS_REQUEST_TIMEOUT_SECONDS", default=60.0, minimum=1.0
        )

        return cls(
            base_url=base_url,
            access_token=access_token,
            per_page=per_page,
            timeout_seconds=timeout,
            output_dir=Path(os.getenv("CANVAS_OUTPUT_DIR", "./acervo")).expanduser(),
            keep_source_html=cls._read_bool("CANVAS_KEEP_SOURCE_HTML", default=True),
            transcription_enabled=cls._read_bool("TRANSCRIPTION_ENABLED", default=True),
            whisper_model=os.getenv("WHISPER_MODEL", "medium").strip() or "medium",
            whisper_language=os.getenv("WHISPER_LANGUAGE", "pt").strip() or "pt",
            whisper_device=os.getenv("WHISPER_DEVICE", "auto").strip() or "auto",
        )

    @staticmethod
    def _read_int(name: str, *, default: int, minimum: int, maximum: int) -> int:
        raw_value = os.getenv(name, str(default)).strip()
        try:
            value = int(raw_value)
        except ValueError as error:
            raise ConfigurationError(f"{name} deve ser um número inteiro.") from error

        if not minimum <= value <= maximum:
            raise ConfigurationError(f"{name} deve estar entre {minimum} e {maximum}.")
        return value

    @staticmethod
    def _read_float(name: str, *, default: float, minimum: float) -> float:
        raw_value = os.getenv(name, str(default)).strip()
        try:
            value = float(raw_value)
        except ValueError as error:
            raise ConfigurationError(f"{name} deve ser um número.") from error

        if value < minimum:
            raise ConfigurationError(f"{name} deve ser maior ou igual a {minimum}.")
        return value

    @staticmethod
    def _read_bool(name: str, *, default: bool) -> bool:
        raw_value = os.getenv(name, str(default)).strip().casefold()
        if raw_value in {"1", "true", "yes", "sim", "on"}:
            return True
        if raw_value in {"0", "false", "no", "nao", "não", "off"}:
            return False
        raise ConfigurationError(f"{name} deve ser true ou false.")
