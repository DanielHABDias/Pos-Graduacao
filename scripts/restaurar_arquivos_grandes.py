"""Restaura materiais acadêmicos maiores que o limite de arquivos do GitHub."""

from __future__ import annotations

import gzip
import hashlib
import os
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATERIAIS = ROOT / "arquivos-grandes"
MODELOS = (
    ROOT
    / "Inteligência Artificial e Aprendizado de Máquina"
    / "06 - Modelos Estatísticos"
    / "03 - UNIDADE 2 - MODELOS LINEARES GENERALIZADOS"
    / "documentos"
)
VISAO = (
    ROOT
    / "Inteligência Artificial e Aprendizado de Máquina"
    / "10 - Análise de Imagem e Visão Computacional"
    / "05 - UNIDADE 4 - APLICAÇÕES COM REDES NEURAIS CONVOLUCIONAIS"
    / "documentos"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_valid(path: Path, expected: str) -> bool:
    return path.is_file() and sha256(path) == expected


def write_atomically(target: Path, writer: object) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(f".{target.name}.restaurando")
    try:
        with temporary.open("wb") as destination:
            writer(destination)
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)


def restore_gzip(source: Path, target: Path, expected: str) -> None:
    if is_valid(target, expected):
        print(f"OK   {target.relative_to(ROOT)}")
        return

    def extract(destination: object) -> None:
        with gzip.open(source, "rb") as compressed:
            shutil.copyfileobj(compressed, destination)

    write_atomically(target, extract)
    if not is_valid(target, expected):
        raise RuntimeError(f"Falha na verificação de {target}")
    print(f"FEITO {target.relative_to(ROOT)}")


def restore_parts(parts: list[Path], target: Path, expected: str) -> None:
    if is_valid(target, expected):
        print(f"OK   {target.relative_to(ROOT)}")
        return

    def join(destination: object) -> None:
        for part in parts:
            with part.open("rb") as source:
                shutil.copyfileobj(source, destination)

    write_atomically(target, join)
    if not is_valid(target, expected):
        raise RuntimeError(f"Falha na verificação de {target}")
    print(f"FEITO {target.relative_to(ROOT)}")


def ensure_copy(source: Path, target: Path, expected: str) -> None:
    if is_valid(target, expected):
        print(f"OK   {target.relative_to(ROOT)}")
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    if not is_valid(target, expected):
        raise RuntimeError(f"Falha na verificação de {target}")
    print(f"FEITO {target.relative_to(ROOT)}")


def main() -> None:
    csv_hash = "429e69fba5a78b6d1663221d095642bc71209ccc77ae5347ed1aaa161a00054d"
    notebook_hash = "0a94abb72c26adbae33246aca77b4d52cc2f1c5bc53dbc8bf91884d7187fac5f"
    dataset_hash = "6de08ebca8a3f1e82f7bf854559ed18fb884d5f3719341468b40ea06a295e518"

    csv = MODELOS / "covid_doencas_preexistentes.csv"
    restore_gzip(
        MATERIAIS / "modelos-estatisticos" / "covid_doencas_preexistentes.csv.gz",
        csv,
        csv_hash,
    )
    ensure_copy(csv, MODELOS / "covid_doencas_preexistentes-canvas-14887837.csv", csv_hash)

    notebook = MODELOS / "04 - Regressão Binária com Python.ipynb"
    restore_gzip(
        MATERIAIS / "modelos-estatisticos" / "regressao-binaria-python.ipynb.gz",
        notebook,
        notebook_hash,
    )
    ensure_copy(
        notebook,
        MODELOS / "04 - Regressão Binária com Python-canvas-14887846.ipynb",
        notebook_hash,
    )

    parts = sorted((MATERIAIS / "visao-computacional").glob("*.part-*"))
    if not parts:
        raise RuntimeError("As partes do conjunto YOLOv4 não foram encontradas")
    restore_parts(parts, VISAO / "yolov4-dataset_car_chair_book.zip", dataset_hash)

    print("\nTodos os arquivos grandes estão íntegros.")


if __name__ == "__main__":
    main()
