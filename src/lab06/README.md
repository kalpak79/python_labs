# ЛР6 - CLI-утилиты с argparse (cat/grep-lite + конвертеры)
### Задание А

### `cli_text.py`
```python
import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text


def check_file(path: str) -> None:
    """Проверяет, что входной файл существует."""
    if not Path(path).is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")


def cmd_cat(path: str, numbered: bool) -> None:
    """Выводит файл построчно, при numbered=True — с номерами."""
    check_file(path)
    text = read_text(path)
    number = 1
    for line in text.splitlines():
        if numbered:
            print(f"{number}. {line}")
        else:
            print(line)
        number += 1


def cmd_stats(path: str, top: int) -> None:
    """Выводит топ-N самых частых слов файла."""
    check_file(path)
    text = read_text(path)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов выводить (по умолчанию 5)")

    args = parser.parse_args()

    if args.command is None:
        parser.error("нужно указать подкоманду: cat или stats")

    try:
        if args.command == "cat":
            cmd_cat(args.input, args.n)
        elif args.command == "stats":
            if args.top <= 0:
                parser.error("--top должно быть положительным числом")
            cmd_stats(args.input, args.top)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
```
1. **Проверка файла:** функция `check_file` проверяет, что входной файл существует. Если его нет, возбуждается `FileNotFoundError` с понятным сообщением.
2. **Подкоманда `cat`:** функция `cmd_cat` читает файл через `read_text` (из ЛР4) и выводит его построчно. Если передан флаг `-n`, перед каждой строкой печатается её номер.
3. **Подкоманда `stats`:** функция `cmd_stats` пропускает текст через `normalize -> tokenize -> count_freq` (из ЛР3), выводит общее число слов, число уникальных слов и топ-N слов через `top_n`. Параметр `--top` по умолчанию равен 5.
4. **Разбор аргументов:** в `main` создаётся `ArgumentParser`, через `add_subparsers(dest="command")` добавляются подкоманды `cat` и `stats`. Каждой подкоманде задаются свои аргументы (`--input`, `-n`, `--top`).
5. **Ошибки:** если подкоманда не указана или `--top` не положительное, вызывается `parser.error(...)`. Если файла нет, `main` перехватывает `FileNotFoundError` и печатает `Ошибка: ...`.

---

### Задание В

### `cli_convert.py`
```python
import argparse

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертеры данных (JSON, CSV, XLSX)")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной .json файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной .csv файл")

    p2 = sub.add_parser("csv2json", help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной .csv файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной .json файл")

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной .csv файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной .xlsx файл")

    args = parser.parse_args()

    if args.cmd is None:
        parser.error("нужно указать подкоманду: json2csv, csv2json или csv2xlsx")

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
        print(f"Готово: {args.input} -> {args.output}")
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден ({e})")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
```
1. **Импорт готовых функций:** конвертеры берутся из ЛР5 (`json_to_csv`, `csv_to_json`, `csv_to_xlsx`).
2. **Подкоманды:** через `add_subparsers(dest="cmd")` создаются `json2csv`, `csv2json` и `csv2xlsx`. У каждой есть обязательные аргументы `--in` и `--out`. Так как `in` является ключевым словом Python, значения сохраняются в `args.input` и `args.output` через параметр `dest`.
3. **Вызов функции:** в зависимости от `args.cmd` вызывается нужная функция из ЛР5. При успехе печатается сообщение `Готово: ... -> ...`.
4. **Ошибки:** `FileNotFoundError` и `ValueError` из функций ЛР5 перехватываются в `main`, выводится понятное сообщение.

---

## Способ запуска

Запуск выполняется из корня репозитория (там, где лежит папка `src/`), с помощью флага `-m`:

```
python -m src.lab06.cli_text <команда> [параметры]
python -m src.lab06.cli_convert <команда> [параметры]
```

| Программа | Команда | Параметры |
|---|---|---|
| `cli_text` | `cat` | `--input <путь>` (обязательный), `-n` (нумерация строк) |
| `cli_text` | `stats` | `--input <путь>` (обязательный), `--top <N>` (по умолчанию 5) |
| `cli_convert` | `json2csv` | `--in <файл.json>`, `--out <файл.csv>` |
| `cli_convert` | `csv2json` | `--in <файл.csv>`, `--out <файл.json>` |
| `cli_convert` | `csv2xlsx` | `--in <файл.csv>`, `--out <файл.xlsx>` |

---

## Тест-кейс А: `cat`

![](images/lab06/)

## Тест-кейс B: `stats`
**Входной файл (`data/lab06/text.txt`):**
```
Кот сидел на окне. Другой кот подошел к окну и тоже сел на окно. 
Первый кот посмотрел на второго кота. Кот, кот, еще один кот!
Окно было чистым, а солнце светило ярко.
```

![](images/lab06/)

## Тест-кейс C: конвертеры
**Команды:**
```
python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv
python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json
python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
```
**Вывод в консоль (для каждой команды):**
```
Готово: data/samples/people.json -> data/out/people.csv
```
**Результат:** в папке `data/out/` созданы файлы `people.csv`, `people.json`, `people.xlsx`.

![](images/lab06/021.png)

## Тест-кейс D: ошибки
**Файл не найден:**
```
python -m src.lab06.cli_text cat --input nope.txt
Ошибка: Файл не найден: nope.txt
```
**Неверное расширение:**
```
python -m src.lab06.cli_convert json2csv --in src/data/samples/people.csv --out x.csv
Ошибка: Неверный формат входного файла: ожидается .json
```
**Неверный аргумент:**
```
python -m src.lab06.cli_text stats --input src/data/samples/people.txt --top 0
usage: cli_text.py [-h] {cat,stats} ...
cli_text.py: error: --top должно быть положительным числом
```
![](images/lab06/error.png)

## Тест-кейс E: `--help`
```
python -m src.lab06.cli_text --help
```
![](images/lab06/help1.png)

```
python -m src.lab06.cli_convert --help
```
![](images/lab06/help2.png)