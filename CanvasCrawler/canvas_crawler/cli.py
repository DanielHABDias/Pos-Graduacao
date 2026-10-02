"""Interface de linha de comando do CanvasCrawler."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable, Sequence
from typing import TypeVar

from canvas_crawler.catalog import CourseCatalog
from canvas_crawler.canvas import CanvasClient
from canvas_crawler.completion import CompletionResult, CourseCompletionService
from canvas_crawler.config import Settings
from canvas_crawler.crawler import CourseCrawler, CrawlResult
from canvas_crawler.exceptions import CanvasCrawlerError
from canvas_crawler.models import Course, ModuleItem, Program

T = TypeVar("T")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="canvas-crawler",
        description="Consulta materiais acadêmicos pela API do Canvas LMS.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("doctor", help="Valida a configuração e o token de acesso.")

    courses_parser = subparsers.add_parser("courses", help="Lista os cursos disponíveis.")
    courses_parser.add_argument(
        "--include-concluded",
        action="store_true",
        help="Inclui cursos cuja matrícula já foi concluída.",
    )
    selection = courses_parser.add_mutually_exclusive_group()
    selection.add_argument(
        "--program",
        metavar="FORMAÇÃO",
        help="Seleciona a formação pela chave ou pelo nome, sem abrir o menu.",
    )
    selection.add_argument(
        "--all",
        action="store_true",
        help="Lista cursos de todas as formações sem abrir o menu.",
    )
    subparsers.add_parser("programs", help="Lista as formações identificadas no Canvas.")
    subparsers.add_parser(
        "inspect",
        help="Navega por formação, disciplina e módulo e lista seus itens.",
    )
    subparsers.add_parser(
        "crawl",
        help="Baixa uma disciplina ou todas as disciplinas de uma formação.",
    )
    subparsers.add_parser(
        "complete",
        help="Conclui itens manuais ou de visualização, exceto avaliações.",
    )
    return parser


def _print_courses(courses: Sequence[Course]) -> None:
    if not courses:
        print("Nenhum curso encontrado.")
        return

    headers = ("ID", "CURSO", "PROGRESSO", "CÓDIGO", "PERÍODO", "ESTADO")
    rows = [
        (
            str(course.id),
            course.name,
            _course_progress_label(course),
            course.course_code or "-",
            course.term_name or "-",
            course.workflow_state,
        )
        for course in courses
    ]
    widths = [max(len(row[index]) for row in [headers, *rows]) for index in range(len(headers))]

    print("  ".join(value.ljust(widths[index]) for index, value in enumerate(headers)))
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)))
    print(f"\nTotal: {len(courses)} disciplina(s).")


def _course_progress_label(course: Course) -> str:
    if course.completion_percentage is None:
        return "indisponível"
    return f"{course.completion_percentage}%"


def _course_selection_label(course: Course) -> str:
    return f"{course.name} — {_course_progress_label(course)}"


def _print_programs(programs: Sequence[Program]) -> None:
    print("FORMAÇÕES DISPONÍVEIS\n")
    for index, program in enumerate(programs, start=1):
        print(f"{index:>2}. {program.name} ({len(program.courses)} disciplina(s))")
        print(f"    chave: {program.key}")


def _print_module_items(items: Sequence[ModuleItem]) -> None:
    if not items:
        print("Este módulo não possui itens visíveis.")
        return

    headers = ("POSIÇÃO", "TIPO", "TÍTULO", "REQUISITO")
    rows = [
        (
            str(item.position),
            item.type,
            item.title,
            item.completion_requirement or "-",
        )
        for item in items
    ]
    widths = [max(len(row[index]) for row in [headers, *rows]) for index in range(len(headers))]
    print("\n" + "  ".join(value.ljust(widths[index]) for index, value in enumerate(headers)))
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)))
    print(f"\nTotal: {len(items)} item(ns). Nenhum conteúdo foi aberto.")


def _choose_option(title: str, options: Sequence[T], label: Callable[[T], str]) -> T:
    if not options:
        raise CanvasCrawlerError(f"Nenhuma opção disponível para {title.casefold()}.")

    print(f"\n{title}:\n")
    for index, option in enumerate(options, start=1):
        print(f"{index:>2}. {label(option)}")

    while True:
        try:
            answer = input("\nEscolha: ").strip()
        except (EOFError, KeyboardInterrupt) as error:
            raise CanvasCrawlerError("Seleção cancelada.") from error

        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print(f"Digite um número entre 1 e {len(options)}.")


def _print_completion_result(result: CompletionResult) -> None:
    print(f"\n{result.course.name}")
    print(f"  Marcados agora: {result.marked}")
    print(f"  Já estavam concluídos: {result.already_completed}")
    print(f"  Provas/atividades ignoradas: {result.assessments_skipped}")
    print(f"  Sem requisito de conclusão compatível: {result.without_manual_completion}")
    print(f"  Bloqueados ou indisponíveis: {result.unavailable}")
    for title in result.unavailable_items:
        print(f"    - {title}")


def _print_crawl_result(result: CrawlResult) -> None:
    print(f"\nDestino: {result.course_root.resolve()}")
    print(f"  Páginas: {result.pages}")
    print(f"  Documentos: {result.files}")
    print(f"  Imagens: {result.images}")
    print(f"  Transcrições: {result.transcripts}")
    print(f"  Artefatos já existentes (não baixados novamente): {result.existing}")
    print(f"  Itens ignorados: {result.skipped}")
    print(f"  Falhas: {result.failures}")
    print(f"  Mídias bloqueadas pelo proprietário: {result.media_blocked}")
    print(f"  Mídias pendentes por provedor ou falha técnica: {result.media_pending}")


def _crawl_menu(client: CanvasClient, settings: Settings, catalog: CourseCatalog) -> None:
    crawler = CourseCrawler(client, settings)

    while True:
        print("\nBAIXAR E ORGANIZAR MATERIAIS\n")
        print("1. Escolher uma disciplina")
        print("2. Baixar todas as disciplinas de uma formação")
        print("0. Voltar ao menu principal")
        try:
            option = input("\nEscolha: ").strip()
        except (EOFError, KeyboardInterrupt) as error:
            raise CanvasCrawlerError("Seleção cancelada.") from error

        if option == "0":
            return
        if option == "1":
            program = _choose_option(
                "Selecione a formação",
                catalog.programs(),
                lambda item: f"{item.name} ({len(item.courses)} disciplinas)",
            )
            course = _choose_option(
                "Selecione a disciplina que será baixada",
                program.courses,
                _course_selection_label,
            )
            confirmation = input(
                f'\nBaixar e organizar "{course.name}"? [s/N]: '
            ).strip().casefold()
            if confirmation in {"s", "sim"}:
                print("\nColetando materiais. Isso pode levar alguns minutos...")
                _print_crawl_result(crawler.crawl(program, course))
            else:
                print("Coleta cancelada.")
            continue
        if option == "2":
            program = _choose_option(
                "Selecione a formação que será baixada",
                catalog.programs(),
                lambda item: f"{item.name} ({len(item.courses)} disciplinas)",
            )
            courses = tuple(program.courses)
            print(
                f'\nEsta operação baixará as {len(courses)} disciplinas de "{program.name}".'
            )
            print("Vídeos podem tornar o processo demorado e usar bastante espaço temporário.")
            confirmation = input('Digite "BAIXAR FORMAÇÃO" para confirmar: ').strip()
            if confirmation != "BAIXAR FORMAÇÃO":
                print("Coleta cancelada.")
                continue

            completed = 0
            failed = 0
            for index, course in enumerate(courses, start=1):
                print(f"\n[{index}/{len(courses)}] {course.name}")
                try:
                    result = crawler.crawl(program, course)
                except (CanvasCrawlerError, OSError, RuntimeError, ValueError) as error:
                    failed += 1
                    print(f"  Falha ao processar a disciplina: {error}")
                    continue
                _print_crawl_result(result)
                completed += 1
                if result.failures:
                    failed += 1
            print(f"\nLote finalizado: {completed} disciplina(s) processada(s).")
            print(f"Disciplinas com falha total ou parcial: {failed}.")
            continue
        print("Digite 0, 1 ou 2.")


def _completion_menu(client: CanvasClient, catalog: CourseCatalog) -> None:
    service = CourseCompletionService(client)

    while True:
        print("\nMARCAR ITENS COMO CONCLUÍDOS\n")
        print("1. Escolher uma disciplina")
        print("2. Marcar todas as disciplinas de uma formação")
        print("0. Voltar ao menu principal")
        try:
            option = input("\nEscolha: ").strip()
        except (EOFError, KeyboardInterrupt) as error:
            raise CanvasCrawlerError("Seleção cancelada.") from error

        if option == "0":
            return
        if option == "1":
            program = _choose_option(
                "Selecione a formação",
                catalog.programs(),
                lambda item: f"{item.name} ({len(item.courses)} disciplinas)",
            )
            course = _choose_option(
                "Selecione a disciplina",
                program.courses,
                _course_selection_label,
            )
            confirmation = input(
                f'\nMarcar os itens manuais de "{course.name}" como concluídos? [s/N]: '
            ).strip().casefold()
            if confirmation in {"s", "sim"}:
                _print_completion_result(service.complete(course))
            else:
                print("Operação cancelada.")
            continue
        if option == "2":
            program = _choose_option(
                "Selecione a formação",
                catalog.programs(),
                lambda item: f"{item.name} ({len(item.courses)} disciplinas)",
            )
            courses = tuple(program.courses)
            print(
                f'\nEsta operação verificará as {len(courses)} disciplinas de "{program.name}".'
            )
            print("Provas, atividades e itens sem conclusão manual serão ignorados.")
            confirmation = input('Digite "CONCLUIR FORMAÇÃO" para confirmar: ').strip()
            if confirmation != "CONCLUIR FORMAÇÃO":
                print("Operação cancelada.")
                continue
            for course in courses:
                _print_completion_result(service.complete(course))
            continue
        print("Digite 0, 1 ou 2.")


def _select_program(programs: Sequence[Program]) -> Program | None:
    """Exibe o menu; retorna None quando o usuário escolhe todos os cursos."""

    print("Selecione a formação cujos cursos deseja listar:\n")
    for index, program in enumerate(programs, start=1):
        print(f"{index:>2}. {program.name} ({len(program.courses)} disciplina(s))")
    print(" 0. Todos os cursos")

    while True:
        try:
            answer = input("\nEscolha: ").strip()
        except (EOFError, KeyboardInterrupt) as error:
            raise CanvasCrawlerError("Seleção cancelada.") from error

        if answer.isdigit():
            selection = int(answer)
            if selection == 0:
                return None
            if 1 <= selection <= len(programs):
                return programs[selection - 1]
        print(f"Digite um número entre 0 e {len(programs)}.")


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    try:
        settings = Settings.from_env()
        with CanvasClient(settings) as client:
            if args.command == "doctor":
                profile = client.get_current_user()
                name = profile.get("name") or profile.get("short_name") or "usuário autenticado"
                print(f"Configuração válida. Autenticado no Canvas como {name}.")
                return 0

            if args.command == "courses":
                catalog = CourseCatalog.from_toml(
                    client.list_courses(include_concluded=args.include_concluded)
                )
                if args.all:
                    selected_courses = catalog.courses
                elif args.program:
                    selected_courses = catalog.find_program(args.program).courses
                elif sys.stdin.isatty():
                    selected_program = _select_program(catalog.programs())
                    selected_courses = (
                        selected_program.courses if selected_program else catalog.courses
                    )
                else:
                    raise CanvasCrawlerError(
                        "O menu interativo exige um terminal. Use --program FORMAÇÃO ou --all."
                    )
                _print_courses(selected_courses)
                return 0

            if args.command == "programs":
                catalog = CourseCatalog.from_toml(client.list_courses())
                _print_programs(catalog.programs())
                return 0

            if args.command == "inspect":
                if not sys.stdin.isatty():
                    raise CanvasCrawlerError("O comando inspect exige um terminal interativo.")

                catalog = CourseCatalog.from_toml(client.list_courses())
                program = _choose_option(
                    "Selecione a formação",
                    catalog.programs(),
                    lambda item: f"{item.name} ({len(item.courses)} disciplinas)",
                )
                course = _choose_option(
                    "Selecione a disciplina",
                    program.courses,
                    _course_selection_label,
                )
                modules = client.list_modules(course.id)
                module = _choose_option(
                    "Selecione o módulo",
                    modules,
                    lambda item: f"{item.name} ({item.items_count} itens)",
                )
                items = client.list_module_items(course.id, module.id)

                print(f"\nFormação: {program.name}")
                print(f"Disciplina: {course.name}")
                print(f"Módulo: {module.name}")
                _print_module_items(items)
                return 0

            if args.command == "crawl":
                if not sys.stdin.isatty():
                    raise CanvasCrawlerError("O comando crawl exige um terminal interativo.")

                catalog = CourseCatalog.from_toml(client.list_courses())
                _crawl_menu(client, settings, catalog)
                return 0

            if args.command == "complete":
                if not sys.stdin.isatty():
                    raise CanvasCrawlerError("O comando complete exige um terminal interativo.")
                catalog = CourseCatalog.from_toml(client.list_courses())
                _completion_menu(client, catalog)
                return 0
    except CanvasCrawlerError as error:
        print(f"Erro: {error}", file=sys.stderr)
        return 1

    return 2
