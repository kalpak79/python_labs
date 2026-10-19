import csv
from pathlib import Path

from ..lab04.io_txt_csv import ensure_parent_dir
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX, задавая ширину столбцов по содержимому."""
    source = Path(csv_path)
    target = Path(xlsx_path)
    ensure_parent_dir(target)

    if source.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался CSV-файл: {source}")
    if target.suffix.lower() != ".xlsx":
        raise ValueError(f"Ожидался XLSX-файл: {target}")

    with source.open("r", newline="", encoding="utf-8") as file:
        sample = file.read(1024) # читаем первые 1024 байта
        file.seek(0) # возвращаемся в начало 

        if not sample.strip():
            raise ValueError("CSV пустой")
        
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;")# sniffer - ищет разделитель

        except csv.Error:
            dialect = csv.excel # стандатртная запятая

        rows = list(csv.reader(file, dialect=dialect)) # Читаем весь файл в список списков строк: rows = [["a","b"], ["1","2"], ...]

    if not rows or not rows[0] or not any(cell.strip() for cell in rows[0]):
        raise ValueError("CSV должен содержать заголовок")

    workbook = Workbook() #Новая Excel-книга
    worksheet = workbook.active
    worksheet.title = "Sheet1"

    for row in rows: # Построчно дописываем данные в конец листа.
        worksheet.append(row)

    for column in worksheet.columns:
        #Для каждого столбца считаем максимальную длину текста среди ячеек:
        max_length = max((len(str(cell.value)) if cell.value is not None else 0) for cell in column)
        worksheet.column_dimensions[column[0].column_letter].width = max(8, max_length)

    workbook.save(target) # Пишет книгу в .xlsx по пути target.

def main():
    csv_to_xlsx("data/lab05/samples/people.csv", "data/lab05/out/people.xlsx")

if __name__ == "__main__":
    main()
