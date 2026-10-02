"""Organização das disciplinas do Canvas em formações acadêmicas reais."""

from __future__ import annotations

import tomllib
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from canvas_crawler.exceptions import ConfigurationError, CanvasCrawlerError
from canvas_crawler.models import Course, Program

DEFAULT_FORMATIONS_FILE = Path(__file__).resolve().parent.parent / "formations.toml"


@dataclass(frozen=True, slots=True)
class FormationRule:
    """Regra declarativa que associa disciplinas a uma formação."""

    key: str
    name: str
    account_ids: frozenset[int]
    term_prefixes: tuple[str, ...]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FormationRule:
        try:
            key = str(data["key"]).strip()
            name = str(data["name"]).strip()
        except KeyError as error:
            raise ConfigurationError("Cada formação precisa de key e name.") from error

        if not key or not name:
            raise ConfigurationError("A chave e o nome da formação não podem ser vazios.")
        return cls(
            key=key,
            name=name,
            account_ids=frozenset(int(value) for value in data.get("account_ids", [])),
            term_prefixes=tuple(str(value) for value in data.get("term_prefixes", [])),
        )

    def matches(self, course: Course) -> bool:
        account_match = course.account_id is not None and course.account_id in self.account_ids
        term_match = bool(course.term_name) and course.term_name.startswith(self.term_prefixes)
        return account_match or term_match


class CourseCatalog:
    """Aplica regras explícitas e mantém itens não classificados separados."""

    def __init__(self, courses: Iterable[Course], rules: Iterable[FormationRule]) -> None:
        self._courses = tuple(courses)
        self._rules = tuple(rules)

    @classmethod
    def from_toml(
        cls, courses: Iterable[Course], path: str | Path = DEFAULT_FORMATIONS_FILE
    ) -> CourseCatalog:
        config_path = Path(path)
        try:
            with config_path.open("rb") as file:
                data = tomllib.load(file)
        except FileNotFoundError as error:
            raise ConfigurationError(f"Arquivo de formações não encontrado: {config_path}") from error
        except tomllib.TOMLDecodeError as error:
            raise ConfigurationError(f"Arquivo de formações inválido: {error}") from error

        raw_rules = data.get("formations")
        if not isinstance(raw_rules, list) or not raw_rules:
            raise ConfigurationError("formations.toml precisa ter ao menos uma [[formations]].")
        rules = [FormationRule.from_dict(item) for item in raw_rules]

        keys = [rule.key for rule in rules]
        if len(keys) != len(set(keys)):
            raise ConfigurationError("As chaves em formations.toml devem ser únicas.")
        return cls(courses, rules)

    @property
    def courses(self) -> tuple[Course, ...]:
        unique = {
            course.id: course
            for program in self.programs()
            for course in program.courses
        }
        return tuple(sorted(unique.values(), key=lambda course: (course.name.casefold(), course.id)))

    def programs(self) -> tuple[Program, ...]:
        programs: list[Program] = []
        for rule in self._rules:
            matches = tuple(
                sorted(
                    (course for course in self._courses if self._matching_rule(course) == rule),
                    key=lambda course: (course.name.casefold(), course.id),
                )
            )
            if matches:
                programs.append(Program(key=rule.key, name=rule.name, courses=matches))
        return tuple(programs)

    def unassigned_courses(self) -> tuple[Course, ...]:
        return tuple(
            course
            for course in self._courses
            if self._matching_rule(course) is None
        )

    def _matching_rule(self, course: Course) -> FormationRule | None:
        """Prioriza IDs de conta específicos antes de regras amplas de período."""

        for rule in self._rules:
            if course.account_id is not None and course.account_id in rule.account_ids:
                return rule
        for rule in self._rules:
            if course.term_name and course.term_name.startswith(rule.term_prefixes):
                return rule
        return None

    def find_program(self, value: str) -> Program:
        query = value.strip().casefold()
        programs = self.programs()
        exact = [
            program
            for program in programs
            if query in {program.key.casefold(), program.name.casefold()}
        ]
        if len(exact) == 1:
            return exact[0]

        partial = [
            program
            for program in programs
            if query in program.key.casefold() or query in program.name.casefold()
        ]
        if len(partial) == 1:
            return partial[0]
        if not partial:
            raise CanvasCrawlerError(f'Formação "{value}" não encontrada.')
        raise CanvasCrawlerError(
            f'Formação "{value}" é ambígua: '
            + ", ".join(program.name for program in partial)
        )
