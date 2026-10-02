"""Modelos de conteúdo retornados pela API do Canvas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Page:
    id: int
    title: str
    url: str
    body: str
    updated_at: str | None

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> Page:
        return cls(
            id=int(data["page_id"]),
            title=str(data.get("title") or data.get("url") or f"Página {data['page_id']}"),
            url=str(data["url"]),
            body=str(data.get("body") or ""),
            updated_at=data.get("updated_at"),
        )


@dataclass(frozen=True, slots=True)
class FileAsset:
    id: int
    display_name: str
    filename: str
    content_type: str
    size: int
    url: str
    updated_at: str | None

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> FileAsset:
        return cls(
            id=int(data["id"]),
            display_name=str(data.get("display_name") or data.get("filename") or data["id"]),
            filename=str(data.get("filename") or data.get("display_name") or data["id"]),
            content_type=str(data.get("content-type") or "application/octet-stream"),
            size=int(data.get("size") or 0),
            url=str(data["url"]),
            updated_at=data.get("updated_at") or data.get("modified_at"),
        )
