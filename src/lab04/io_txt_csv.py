from ..lib import testing
from ..lib.text import normalize, tokenize, top_n, count_freq

import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:


    p = Path(path)
    return p.read_text(encoding=encoding)

    """Прочитать как одну строку.
    
        Кодировка по умолчанию — UTF-8. 
    
        Если файл в другой кодировке
        read_text("data/input.txt", encoding="cp1251")
    
        Исключения (FileNotFoundError и UnicodeDecodeError не подавляются
        
    """


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Записать строки в CSV (разделитель ','). Перезаписывает файл.

    Если передан header — он записывается первой строкой.
    Все строки должны иметь одинаковую длину, иначе ValueError.
    """

    rows = list(rows)

    # Проверка одинаковой длины всех строк (включая header, если он задан)
    lengths = {len(r) for r in rows}
    if header is not None:
        lengths.add(len(header))

    if len(lengths) > 1:
        raise ValueError("Все строки должны иметь одинаковую длину")


    ensure_parent_dir(path) 
    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории для path, если их ещё нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)

#ensure_parent_dir извлекает путь к содержащей папке целевого файла с помощью свойства .parent. 
# Создает эту директорию методом .mkdir(). Флаг parents=True отвечает за рекурсивное создание вложенных папок, а exist_ok=True игнорирует ошибку, если папка уже существует.