"""Agrupamento de cursos pertencentes à mesma formação."""

from __future__ import annotations

from dataclasses import dataclass

from canvas_crawler.models.course import Course


@dataclass(frozen=True, slots=True)
class Program:
    """Formação acadêmica inferida a partir dos metadados do Canvas."""

    key: str
    name: str
    courses: tuple[Course, ...]
