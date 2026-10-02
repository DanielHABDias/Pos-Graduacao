from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from canvas_crawler.media import CanvasStudioResolver, save_caption_transcript


class MediaTests(unittest.TestCase):
    def test_converts_webvtt_to_markdown_and_json(self) -> None:
        content = """WEBVTT

00:00:01.000 --> 00:00:03.500
Olá, turma.

00:01:02,000 --> 00:01:05,000
Segundo trecho.
"""
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "aula.md"
            save_caption_transcript(content, output, title="Aula")

            self.assertIn("**[00:00:01]** Olá, turma.", output.read_text(encoding="utf-8"))
            data = json.loads(output.with_suffix(".json").read_text(encoding="utf-8"))
            self.assertEqual(len(data["segments"]), 2)
            self.assertEqual(data["segments"][1]["start"], 62.0)

    def test_recognizes_only_canvas_studio_lti_embed(self) -> None:
        self.assertTrue(
            CanvasStudioResolver.supports(
                "https://canvas.example/courses/1/external_tools/retrieve?"
                "url=https%3A%2F%2Ftenant.instructuremedia.com%2Flti%2Flaunch"
            )
        )
        self.assertFalse(CanvasStudioResolver.supports("https://www.youtube.com/embed/1"))


if __name__ == "__main__":
    unittest.main()
