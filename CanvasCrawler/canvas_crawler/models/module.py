"""Modelos de módulo e item de módulo do Canvas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Module:
    id: int
    name: str
    position: int
    state: str
    items_count: int

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> Module:
        return cls(
            id=int(data["id"]),
            name=str(data.get("name") or f"Módulo {data['id']}"),
            position=int(data.get("position") or 0),
            state=str(data.get("state") or "unknown"),
            items_count=int(data.get("items_count") or 0),
        )


@dataclass(frozen=True, slots=True)
class ModuleItem:
    id: int
    module_id: int
    title: str
    type: str
    position: int
    completion_requirement: str | None
    completion_requirement_met: bool | None
    content_id: int | None
    page_url: str | None
    external_url: str | None
    html_url: str | None

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> ModuleItem:
        requirement = data.get("completion_requirement") or {}
        return cls(
            id=int(data["id"]),
            module_id=int(data["module_id"]),
            title=str(data.get("title") or f"Item {data['id']}"),
            type=str(data.get("type") or "Unknown"),
            position=int(data.get("position") or 0),
            completion_requirement=(
                str(requirement["type"]) if requirement.get("type") else None
            ),
            completion_requirement_met=(
                bool(requirement["completed"])
                if "completed" in requirement
                else None
            ),
            content_id=int(data["content_id"]) if data.get("content_id") is not None else None,
            page_url=str(data["page_url"]) if data.get("page_url") else None,
            external_url=str(data["external_url"]) if data.get("external_url") else None,
            html_url=str(data["html_url"]) if data.get("html_url") else None,
        )
