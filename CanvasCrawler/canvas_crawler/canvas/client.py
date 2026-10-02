"""Cliente HTTP orientado a objetos para a API REST do Canvas."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx

from canvas_crawler.config import Settings
from canvas_crawler.exceptions import AuthenticationError, CanvasApiError
from canvas_crawler.models import Course, FileAsset, Module, ModuleItem, Page


class CanvasClient:
    """Centraliza autenticação, requisições e paginação do Canvas."""

    def __init__(self, settings: Settings, *, http_client: httpx.Client | None = None) -> None:
        self._settings = settings
        self._owns_http_client = http_client is None
        self._http = http_client or httpx.Client(
            base_url=settings.base_url,
            headers={
                "Authorization": f"Bearer {settings.access_token}",
                "Accept": "application/json",
                "User-Agent": "CanvasCrawler/0.1",
            },
            follow_redirects=True,
            timeout=settings.timeout_seconds,
        )

    def __enter__(self) -> CanvasClient:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def close(self) -> None:
        """Fecha conexões criadas pelo próprio cliente."""

        if self._owns_http_client:
            self._http.close()

    def get_current_user(self) -> dict[str, Any]:
        """Retorna o perfil mínimo usado para validar a autenticação."""

        data = self._get_json("/api/v1/users/self/profile")
        if not isinstance(data, dict):
            raise CanvasApiError("O Canvas retornou um perfil em formato inesperado.")
        return data

    def list_courses(self, *, include_concluded: bool = False) -> list[Course]:
        """Lista os cursos do usuário, percorrendo todas as páginas da API."""

        params: list[tuple[str, str | int]] = [
            ("include[]", "account"),
            ("include[]", "term"),
            ("include[]", "course_progress"),
            ("per_page", self._settings.per_page),
        ]
        if include_concluded:
            params.append(("include[]", "concluded"))
        else:
            params.append(("enrollment_state[]", "active"))

        courses = [Course.from_api(item) for item in self._get_paginated("/api/v1/courses", params)]
        return sorted(courses, key=lambda course: (course.name.casefold(), course.id))

    def list_modules(self, course_id: int) -> list[Module]:
        """Lista os módulos de uma disciplina sem buscar seus conteúdos."""

        params: list[tuple[str, str | int]] = [("per_page", self._settings.per_page)]
        modules = [
            Module.from_api(item)
            for item in self._get_paginated(
                f"/api/v1/courses/{course_id}/modules", params
            )
        ]
        return sorted(modules, key=lambda module: (module.position, module.id))

    def list_module_items(self, course_id: int, module_id: int) -> list[ModuleItem]:
        """Lista apenas metadados dos itens de um módulo."""

        params: list[tuple[str, str | int]] = [("per_page", self._settings.per_page)]
        items = [
            ModuleItem.from_api(item)
            for item in self._get_paginated(
                f"/api/v1/courses/{course_id}/modules/{module_id}/items", params
            )
        ]
        return sorted(items, key=lambda item: (item.position, item.id))

    def get_page(self, course_id: int, page_url: str) -> Page:
        data = self._get_json(f"/api/v1/courses/{course_id}/pages/{page_url}")
        if not isinstance(data, dict):
            raise CanvasApiError("O Canvas retornou uma página em formato inesperado.")
        return Page.from_api(data)

    def get_file(self, file_id: int) -> FileAsset:
        data = self._get_json(f"/api/v1/files/{file_id}")
        if not isinstance(data, dict):
            raise CanvasApiError("O Canvas retornou um arquivo em formato inesperado.")
        return FileAsset.from_api(data)

    def list_media_attachments(self, course_id: int) -> list[dict[str, Any]]:
        return list(
            self._get_paginated(
                f"/api/v1/courses/{course_id}/media_attachments",
                [("per_page", self._settings.per_page)],
            )
        )

    def list_media_tracks(self, attachment_id: int) -> list[dict[str, Any]]:
        data = self._get_json(
            f"/api/v1/media_attachments/{attachment_id}/media_tracks",
            params=[("include[]", "content"), ("include[]", "webvtt_content")],
        )
        if not isinstance(data, list):
            raise CanvasApiError("O Canvas retornou faixas de mídia em formato inesperado.")
        return [item for item in data if isinstance(item, dict)]

    def mark_module_item_done(self, course_id: int, module_id: int, item_id: int) -> None:
        """Marca um item com requisito ``must_mark_done`` como concluído."""

        self._request(
            "PUT",
            f"/api/v1/courses/{course_id}/modules/{module_id}/items/{item_id}/done",
        )

    def mark_module_item_read(self, course_id: int, module_id: int, item_id: int) -> None:
        """Registra a visualização de um item com requisito ``must_view``."""

        self._request(
            "POST",
            f"/api/v1/courses/{course_id}/modules/{module_id}/items/{item_id}/mark_read",
        )

    def get_sessionless_launch_url(self, course_id: int, target_url: str) -> str:
        """Obtém no Canvas uma URL LTI temporária sem compartilhar o bearer token."""

        response = self._get_json(
            f"/api/v1/courses/{course_id}/external_tools/sessionless_launch",
            params={"url": target_url},
        )
        if not isinstance(response, dict) or not response.get("url"):
            raise CanvasApiError("O Canvas não retornou uma URL de lançamento LTI.")
        return str(response["url"])

    def download(self, url: str, destination: Path) -> str:
        """Baixa uma URL sem enviar o token do Canvas a domínios externos."""

        parsed = urlparse(url)
        expected = urlparse(self._settings.base_url)
        if parsed.scheme not in {"http", "https"}:
            raise CanvasApiError(f"Protocolo de download não permitido: {parsed.scheme}")

        is_canvas_url = (parsed.scheme, parsed.netloc) == (expected.scheme, expected.netloc)
        external_client: httpx.Client | None = None
        client = self._http
        if not is_canvas_url:
            external_client = httpx.Client(
                follow_redirects=True,
                timeout=self._settings.timeout_seconds,
                headers={"User-Agent": "CanvasCrawler/0.1"},
            )
            client = external_client

        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_name(f".{destination.name}.part")
        try:
            with client.stream("GET", url) as response:
                if response.status_code in {401, 403}:
                    raise AuthenticationError("O Canvas recusou o download do arquivo.")
                response.raise_for_status()
                with temporary.open("wb") as file:
                    for chunk in response.iter_bytes():
                        file.write(chunk)
                content_type = response.headers.get("content-type", "application/octet-stream")
            temporary.replace(destination)
            return content_type.split(";", maxsplit=1)[0].strip()
        except httpx.HTTPError as error:
            temporary.unlink(missing_ok=True)
            raise CanvasApiError(f"Não foi possível baixar {parsed.netloc}: {error}") from error
        finally:
            if external_client is not None:
                external_client.close()

    def _get_paginated(
        self, path: str, params: list[tuple[str, str | int]]
    ) -> Iterator[dict[str, Any]]:
        next_url: str | None = path
        next_params: list[tuple[str, str | int]] | None = params

        while next_url:
            response = self._request("GET", next_url, params=next_params)
            payload = self._decode_json(response)
            if not isinstance(payload, list):
                raise CanvasApiError("O Canvas retornou uma página em formato inesperado.")

            for item in payload:
                if not isinstance(item, dict):
                    raise CanvasApiError("O Canvas retornou um item em formato inesperado.")
                yield item

            next_link = response.links.get("next")
            next_url = next_link.get("url") if next_link else None
            next_params = None
            if next_url:
                self._validate_pagination_url(next_url)

    def _get_json(self, path: str, **kwargs: Any) -> Any:
        return self._decode_json(self._request("GET", path, **kwargs))

    def _request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        try:
            response = self._http.request(method, url, **kwargs)
        except httpx.TimeoutException as error:
            raise CanvasApiError("A requisição ao Canvas excedeu o tempo limite.") from error
        except httpx.RequestError as error:
            raise CanvasApiError(f"Não foi possível acessar o Canvas: {error}") from error

        if response.status_code in {401, 403}:
            raise AuthenticationError(
                "O Canvas recusou o token. Confirme CANVAS_ACCESS_TOKEN e suas permissões."
            )

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as error:
            request_id = response.headers.get("X-Request-Context", "não informado")
            raise CanvasApiError(
                f"A API do Canvas respondeu HTTP {response.status_code} "
                f"(request id: {request_id})."
            ) from error
        return response

    @staticmethod
    def _decode_json(response: httpx.Response) -> Any:
        try:
            return response.json()
        except ValueError as error:
            raise CanvasApiError("O Canvas retornou uma resposta que não é JSON válido.") from error

    def _validate_pagination_url(self, url: str) -> None:
        expected = urlparse(self._settings.base_url)
        received = urlparse(url)
        if (received.scheme, received.netloc) != (expected.scheme, expected.netloc):
            raise CanvasApiError("O Canvas retornou paginação para um domínio inesperado.")
