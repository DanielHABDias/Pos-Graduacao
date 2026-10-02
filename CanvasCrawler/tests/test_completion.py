from __future__ import annotations

import unittest

from canvas_crawler.completion import CourseCompletionService
from canvas_crawler.exceptions import CanvasApiError
from canvas_crawler.models import Course, Module, ModuleItem


def item(
    item_id: int,
    item_type: str,
    requirement: str | None,
    completed: bool | None,
) -> ModuleItem:
    return ModuleItem(
        id=item_id,
        module_id=20,
        title=f"Item {item_id}",
        type=item_type,
        position=item_id,
        completion_requirement=requirement,
        completion_requirement_met=completed,
        content_id=None,
        page_url=None,
        external_url=None,
        html_url=None,
    )


class FakeClient:
    def __init__(self) -> None:
        self.marked: list[int] = []
        self.items = [
            item(1, "Page", "must_mark_done", False),
            item(2, "Page", "must_mark_done", True),
            item(3, "Quiz", "must_mark_done", False),
            item(4, "Page", "must_view", False),
            item(5, "File", None, None),
            item(6, "Page", "must_mark_done", False),
        ]

    def list_modules(self, _: int) -> list[Module]:
        return [Module(20, "Módulo", 1, "active", len(self.items))]

    def list_module_items(self, _: int, __: int) -> list[ModuleItem]:
        return self.items

    def mark_module_item_done(self, _: int, __: int, item_id: int) -> None:
        if item_id == 6:
            raise CanvasApiError("bloqueado")
        self.marked.append(item_id)


class CompletionServiceTests(unittest.TestCase):
    def test_marks_only_incomplete_manual_non_assessment_items(self) -> None:
        client = FakeClient()
        course = Course(10, "Disciplina", "D", "available", 1, None, None, None, None)

        result = CourseCompletionService(client).complete(course)  # type: ignore[arg-type]

        self.assertEqual(client.marked, [1])
        self.assertEqual(result.marked, 1)
        self.assertEqual(result.already_completed, 1)
        self.assertEqual(result.assessments_skipped, 1)
        self.assertEqual(result.without_manual_completion, 2)
        self.assertEqual(result.unavailable, 1)


if __name__ == "__main__":
    unittest.main()
