import csv
import json
from pathlib import Path
from typing import Iterable, Union


def replace_extension(path: Union[str, Path], new_ext: str = "") -> Path:
    extensions = "".join(Path(path).suffixes)
    return Path(str(path).replace(extensions, new_ext))


def append_extension(filename: str, ext: str):
    if not '.' in filename:
        return filename + f'.{ext}'
    if not filename.endswith(ext):
        return replace_extension(filename, ext)
    return filename


def save_to_csv(content: Iterable[dict], filename):
    """
    :param content:
        Iterable из словарей, каждый из которых содержит ссылку и контент статьи
    :param filename:
        Имя файла для записи
    :return:
        None
    """
    filename = append_extension(filename, 'csv')
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Ссылка', 'Тип+Текст'])
        for article in content:
            value = article.popitem()
            link = value[0]  # Ссылка
            tag_text = value[1]  # (формат, текст)
            writer.writerow([link, tag_text])


def save_to_json(content: Iterable[dict], filename):
    """
    :param content:
        Iterable из словарей, каждый из которых содержит ссылку и контент статьи
    :param filename:
        Имя файла для записи
    :return:
        None
    """
    filename = append_extension(filename, 'json')
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)
