from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from canvas_crawler.catalog import CourseCatalog, FormationRule
from canvas_crawler.exceptions import CanvasCrawlerError, ConfigurationError
from canvas_crawler.models import Course


def make_course(
    course_id: int,
    name: str,
    account_id: int,
    term_name: str,
) -> Course:
    return Course(
        id=course_id,
        name=name,
        course_code=name,
        workflow_state="available",
        account_id=account_id,
        account_name="Conta",
        term_name=term_name,
        start_at=None,
        end_at=None,
    )


class CourseCatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ads = FormationRule(
            key="ads",
            name="Tecnologia em Análise e Desenvolvimento de Sistemas",
            account_ids=frozenset(),
            term_prefixes=("Graduação Presencial", "Semipresencial"),
        )
        self.ai = FormationRule(
            key="ia-pos",
            name="Inteligência Artificial e Aprendizado de Máquina",
            account_ids=frozenset({14586}),
            term_prefixes=(),
        )

    def test_organizes_courses_into_two_real_formations(self) -> None:
        catalog = CourseCatalog(
            [
                make_course(1, "Disciplina compartilhada de Sistemas", 10720, "Graduação Presencial Síncrona - 2023/2"),
                make_course(2, "Data Discovery", 14586, "Pós-graduação EAD - 2025/1"),
            ],
            [self.ads, self.ai],
        )

        programs = catalog.programs()

        self.assertEqual([program.key for program in programs], ["ads", "ia-pos"])
        self.assertEqual(programs[0].courses[0].id, 1)
        self.assertEqual(programs[1].courses[0].id, 2)

    def test_keeps_global_and_extension_courses_unassigned(self) -> None:
        global_course = make_course(3, "Guia do Canvas", 129, "Período padrão")
        extension = make_course(4, "IA Aplicada", 16882, "Extensão EAD - 2025/1")
        catalog = CourseCatalog([global_course, extension], [self.ads, self.ai])

        self.assertEqual(catalog.programs(), ())
        self.assertEqual(catalog.unassigned_courses(), (global_course, extension))

    def test_specific_account_can_define_a_future_undergraduate_program(self) -> None:
        future_program = FormationRule(
            key="third-degree",
            name="Terceira graduação",
            account_ids=frozenset({999}),
            term_prefixes=(),
        )
        catalog = CourseCatalog(
            [make_course(5, "Nova disciplina", 999, "Graduação Presencial - 2027/1")],
            [self.ads, self.ai, future_program],
        )

        programs = catalog.programs()

        self.assertEqual([program.key for program in programs], ["third-degree"])

    def test_finds_program_by_key(self) -> None:
        catalog = CourseCatalog(
            [make_course(1, "Data Discovery", 14586, "Pós-graduação EAD - 2025/1")],
            [self.ads, self.ai],
        )

        self.assertEqual(catalog.find_program("ia-pos").courses[0].id, 1)

    def test_reports_unknown_program(self) -> None:
        catalog = CourseCatalog([], [self.ads, self.ai])

        with self.assertRaises(CanvasCrawlerError):
            catalog.find_program("inexistente")

    def test_loads_rules_from_toml(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "formations.toml"
            path.write_text(
                '[[formations]]\nkey="ads"\nname="ADS"\nterm_prefixes=["Graduação"]\n',
                encoding="utf-8",
            )
            catalog = CourseCatalog.from_toml(
                [make_course(1, "Disciplina", 1, "Graduação - 2025/1")], path
            )

        self.assertEqual(catalog.programs()[0].key, "ads")

    def test_rejects_missing_rules_file(self) -> None:
        with self.assertRaises(ConfigurationError):
            CourseCatalog.from_toml([], "does-not-exist.toml")


if __name__ == "__main__":
    unittest.main()
