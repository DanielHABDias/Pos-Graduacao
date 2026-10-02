from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from canvas_crawler.config import Settings
from canvas_crawler.crawler import CourseCrawler
from canvas_crawler.models import (
    Course,
    FileAsset,
    Module,
    ModuleItem,
    Page,
    Program,
)


def module_item(
    item_id: int,
    title: str,
    item_type: str,
    position: int,
    *,
    content_id: int | None = None,
    page_url: str | None = None,
) -> ModuleItem:
    return ModuleItem(
        id=item_id,
        module_id=100,
        title=title,
        type=item_type,
        position=position,
        completion_requirement=None,
        completion_requirement_met=None,
        content_id=content_id,
        page_url=page_url,
        external_url=None,
        html_url=None,
    )


class FakeCanvasClient:
    def __init__(self) -> None:
        self.module = Module(id=100, name="Introdução", position=1, state="active", items_count=4)
        self.items = [
            module_item(1, "Aula inicial", "Page", 1, page_url="aula-inicial"),
            module_item(2, "Apostila", "File", 2, content_id=12),
            module_item(3, "Videoaula", "File", 3, content_id=13),
            module_item(4, "Prova", "Quiz", 4),
        ]
        self.files = {
            11: FileAsset(11, "Diagrama.png", "diagrama.png", "image/png", 3, "https://files/11", None),
            12: FileAsset(12, "Apostila.pdf", "apostila.pdf", "application/pdf", 3, "https://files/12", None),
            13: FileAsset(13, "Videoaula.mp4", "videoaula.mp4", "video/mp4", 3, "https://files/13", None),
        }

    def list_modules(self, _: int) -> list[Module]:
        return [self.module]

    def list_module_items(self, _: int, __: int) -> list[ModuleItem]:
        return self.items

    def get_page(self, _: int, __: str) -> Page:
        return Page(
            id=20,
            title="Aula inicial",
            url="aula-inicial",
            body=(
                '<p>Conteúdo da aula.</p><img src="/files/11/download" alt="Diagrama">'
                '<a href="/files/12/download">Apostila</a>'
            ),
            updated_at=None,
        )

    def get_file(self, file_id: int) -> FileAsset:
        return self.files[file_id]

    def download(self, url: str, destination: Path) -> str:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(b"abc")
        if url.endswith("11"):
            return "image/png"
        if url.endswith("13"):
            return "video/mp4"
        return "application/pdf"


class FakeTranscriber:
    def transcribe(self, video: Path, output: Path, *, title: str) -> Path:
        if not video.exists():
            raise AssertionError("O vídeo temporário deve existir durante a transcrição.")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(f"# {title}\n\nTranscrição.\n", encoding="utf-8")
        output.with_suffix(".json").write_text("{}\n", encoding="utf-8")
        return output


class CourseCrawlerTests(unittest.TestCase):
    def test_creates_portable_tree_and_deletes_temporary_video(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "acervo"
            settings = Settings(
                base_url="https://canvas.example.edu",
                access_token="token",
                output_dir=output,
            )
            course = Course(
                id=10,
                name="01 - Disciplina",
                course_code="DISC01",
                workflow_state="available",
                account_id=1,
                account_name="Formação",
                term_name="2026/1",
                start_at=None,
                end_at=None,
            )
            program = Program("formacao", "Minha Formação", (course,))
            crawler = CourseCrawler(FakeCanvasClient(), settings)  # type: ignore[arg-type]
            crawler._transcriber = FakeTranscriber()  # type: ignore[assignment]

            result = crawler.crawl(program, course)

            self.assertEqual(result.pages, 1)
            self.assertEqual(result.files, 1)
            self.assertEqual(result.images, 1)
            self.assertEqual(result.transcripts, 1)
            self.assertEqual(result.skipped, 1)
            self.assertTrue((result.course_root / "README.md").exists())
            module_root = result.course_root / "01 - Introdução"
            self.assertTrue((module_root / "paginas/01 - Aula inicial.md").exists())
            self.assertTrue((module_root / "html/01 - Aula inicial.html").exists())
            self.assertTrue((module_root / "images/Diagrama.png").exists())
            self.assertTrue((module_root / "documentos/Apostila.pdf").exists())
            self.assertTrue((module_root / "transcricoes/Videoaula.md").exists())
            self.assertFalse(list((output / ".tmp").glob("*")))
            self.assertFalse(list(result.course_root.rglob("*.mp4")))

            crawler.crawl(program, course)
            self.assertFalse(list(result.course_root.rglob("*-canvas-*")))
            manifest = json.loads(
                (result.course_root / ".canvas/manifest.json").read_text(encoding="utf-8")
            )
            artifacts = [entry["artifact"] for entry in manifest["items"]]
            self.assertIn("image", artifacts)
            self.assertIn("document", artifacts)
            self.assertIn("transcript", artifacts)


if __name__ == "__main__":
    unittest.main()
