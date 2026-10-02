"""Layout portátil, nomenclatura e manifesto do acervo coletado."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from canvas_crawler.models import Course, Module, Program


class NamingPolicy:
    """Gera nomes legíveis sem permitir caminhos perigosos."""

    _INVALID = re.compile(r"[<>:\"/\\|?*\x00-\x1f]")

    @classmethod
    def clean(cls, value: str, *, fallback: str, limit: int = 120) -> str:
        value = unicodedata.normalize("NFC", value).strip()
        value = cls._INVALID.sub("_", value)
        value = re.sub(r"\s+", " ", value).strip(" .")
        return (value or fallback)[:limit].rstrip(" .")

    @classmethod
    def numbered(cls, position: int, title: str, *, fallback: str) -> str:
        clean_title = cls.clean(title, fallback=fallback)
        return f"{position:02d} - {clean_title}"

    @staticmethod
    def sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()


@dataclass(frozen=True, slots=True)
class ModuleWorkspace:
    root: Path
    pages: Path
    html: Path
    documents: Path
    images: Path
    transcripts: Path

    @classmethod
    def create(cls, course_root: Path, module: Module) -> ModuleWorkspace:
        root = course_root / NamingPolicy.numbered(
            module.position, module.name, fallback=f"Módulo {module.id}"
        )
        workspace = cls(
            root=root,
            pages=root / "paginas",
            html=root / "html",
            documents=root / "documentos",
            images=root / "images",
            transcripts=root / "transcricoes",
        )
        root.mkdir(parents=True, exist_ok=True)
        return workspace

    def ensure(self, directory: Path) -> Path:
        directory.mkdir(parents=True, exist_ok=True)
        return directory


@dataclass(frozen=True, slots=True)
class CourseWorkspace:
    formation_root: Path
    course_root: Path
    metadata_dir: Path

    @classmethod
    def create(cls, output_root: Path, program: Program, course: Course) -> CourseWorkspace:
        formation_root = output_root / NamingPolicy.clean(
            program.name, fallback=f"Formação {program.key}"
        )
        course_root = formation_root / NamingPolicy.clean(
            course.name, fallback=f"Disciplina {course.id}"
        )
        metadata_dir = course_root / ".canvas"
        metadata_dir.mkdir(parents=True, exist_ok=True)
        return cls(formation_root, course_root, metadata_dir)


class Manifest:
    """Registro incremental do que foi coletado e ignorado."""

    def __init__(self, path: Path, *, program: Program, course: Course) -> None:
        self._path = path
        self._data: dict[str, Any] = {
            "schema_version": 1,
            "formation": {"key": program.key, "name": program.name},
            "course": {"id": course.id, "name": course.name, "code": course.course_code},
            "updated_at": None,
            "items": [],
        }
        if path.exists():
            try:
                existing = json.loads(path.read_text(encoding="utf-8"))
                if existing.get("schema_version") == 1:
                    self._data = existing
            except (json.JSONDecodeError, OSError):
                pass

    def record(self, entry: dict[str, Any]) -> None:
        items = self._data.setdefault("items", [])
        identity = self._identity(entry)
        items[:] = [
            item
            for item in items
            if self._identity(item) != identity
        ]
        items.append(entry)
        self.save()

    @staticmethod
    def _identity(entry: dict[str, Any]) -> tuple[Any, ...]:
        """Distingue, por exemplo, várias imagens pertencentes à mesma página."""
        return (
            entry.get("module_id"),
            entry.get("item_id"),
            entry.get("artifact"),
            entry.get("canvas_file_id"),
            entry.get("path"),
            entry.get("url"),
            entry.get("media_key"),
        )

    def save(self) -> None:
        self._data["updated_at"] = datetime.now(UTC).isoformat()
        temporary = self._path.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary.replace(self._path)

    def remove_media_pending(self, *, module_id: int, item_id: int, media_key: str) -> None:
        self.remove_media_unavailable(
            module_id=module_id, item_id=item_id, media_key=media_key
        )

    def remove_media_unavailable(self, *, module_id: int, item_id: int, media_key: str) -> None:
        items = self._data.setdefault("items", [])
        remaining = [
            entry
            for entry in items
            if not (
                entry.get("module_id") == module_id
                and entry.get("item_id") == item_id
                and entry.get("artifact") in {"media-pending", "media-blocked"}
                and entry.get("media_key") == media_key
            )
        ]
        if len(remaining) != len(items):
            items[:] = remaining
            self.save()
