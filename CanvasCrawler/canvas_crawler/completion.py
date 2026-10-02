"""Conclusão explícita e segura de itens de módulo no Canvas."""

from __future__ import annotations

from dataclasses import dataclass, field

from canvas_crawler.canvas import CanvasClient
from canvas_crawler.exceptions import CanvasCrawlerError
from canvas_crawler.models import Course


@dataclass(slots=True)
class CompletionResult:
    course: Course
    marked: int = 0
    already_completed: int = 0
    assessments_skipped: int = 0
    without_manual_completion: int = 0
    unavailable: int = 0
    unavailable_items: list[str] = field(default_factory=list)


class CourseCompletionService:
    """Conclui itens seguros com requisitos manuais ou de visualização."""

    _ASSESSMENT_TYPES = {"Assignment", "Quiz", "Discussion"}
    _MANUAL_REQUIREMENT = "must_mark_done"
    _VIEW_REQUIREMENT = "must_view"

    def __init__(self, client: CanvasClient) -> None:
        self._client = client

    def complete(self, course: Course) -> CompletionResult:
        result = CompletionResult(course=course)

        try:
            modules = self._client.list_modules(course.id)
        except CanvasCrawlerError:
            result.unavailable += 1
            result.unavailable_items.append("A disciplina não permitiu consultar seus módulos")
            return result

        for module in modules:
            try:
                items = self._client.list_module_items(course.id, module.id)
            except CanvasCrawlerError:
                result.unavailable += 1
                result.unavailable_items.append(f"{module.name} — módulo indisponível")
                continue

            for item in items:
                if item.type in self._ASSESSMENT_TYPES:
                    result.assessments_skipped += 1
                    continue
                if item.completion_requirement not in {
                    self._MANUAL_REQUIREMENT,
                    self._VIEW_REQUIREMENT,
                }:
                    result.without_manual_completion += 1
                    continue
                if item.completion_requirement_met is True:
                    result.already_completed += 1
                    continue

                try:
                    if item.completion_requirement == self._VIEW_REQUIREMENT:
                        self._client.mark_module_item_read(course.id, module.id, item.id)
                    else:
                        self._client.mark_module_item_done(course.id, module.id, item.id)
                except CanvasCrawlerError:
                    # Itens bloqueados, não publicados ou recusados pelo Canvas são ignorados.
                    result.unavailable += 1
                    result.unavailable_items.append(f"{module.name} — {item.title}")
                else:
                    result.marked += 1

        return result
