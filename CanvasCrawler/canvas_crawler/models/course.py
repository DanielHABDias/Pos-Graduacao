"""Modelo de leitura para um curso do Canvas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Course:
    """Dados relevantes para identificar e selecionar um curso."""

    id: int
    name: str
    course_code: str
    workflow_state: str
    account_id: int | None
    account_name: str | None
    term_name: str | None
    start_at: str | None
    end_at: str | None

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> Course:
        """Converte a resposta do Canvas para um modelo previsível."""

        account = data.get("account") or {}
        term = data.get("term") or {}
        return cls(
            id=int(data["id"]),
            name=str(data.get("name") or data.get("course_code") or f"Curso {data['id']}"),
            course_code=str(data.get("course_code") or ""),
            workflow_state=str(data.get("workflow_state") or "unknown"),
            account_id=int(account["id"]) if account.get("id") is not None else None,
            account_name=str(account["name"]) if account.get("name") else None,
            term_name=str(term["name"]) if term.get("name") else None,
            start_at=data.get("start_at"),
            end_at=data.get("end_at"),
        )
