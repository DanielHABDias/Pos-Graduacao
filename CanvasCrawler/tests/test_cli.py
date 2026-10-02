from __future__ import annotations

import unittest

from canvas_crawler.cli import _course_selection_label
from canvas_crawler.models import Course


class CourseSelectionLabelTests(unittest.TestCase):
    def make_course(self, completion_percentage: int | None) -> Course:
        return Course(
            10,
            "Machine Learning",
            "ML",
            "available",
            1,
            "Conta",
            "2026/2",
            None,
            None,
            completion_percentage,
        )

    def test_displays_percentage_next_to_course_name(self) -> None:
        self.assertEqual(
            _course_selection_label(self.make_course(80)),
            "Machine Learning — 80%",
        )

    def test_reports_unavailable_progress(self) -> None:
        self.assertEqual(
            _course_selection_label(self.make_course(None)),
            "Machine Learning — indisponível",
        )


if __name__ == "__main__":
    unittest.main()
