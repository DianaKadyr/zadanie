import random
import configparser
import json
from faker import Faker


def main_func(pk: int = 1) -> None:
    """формирует список из 100 словарей и записывает его в json файл"""
    config = configparser.ConfigParser()
    config.read("conf.py")
    list_ = []
    for i in range(100):
        dict_ = {'model': config["Model"]["model"],
                 'pk': pk,
                 'fields': {'title': func_title(),
                            'year': func_year(),
                            'pages': func_pages(),
                            'isbn13': func_isbn13(),
                            'rating': func_rating(),
                            'price': func_price(),
                            'discount': func_discount(),
                            'author': func_author()}}
        print(json.dumps(dict_, indent=4, ensure_ascii=False))
        list_ += [dict_]
        pk += 1
    with open("output.json", "w") as output_f:
        json.dump(list_, output_f, indent=4, ensure_ascii=False)


def func_title() -> str:
    """генерирует название книги, список которой находится в books.txt"""
    lines = []
    with open("books.txt", "r") as file:
        for line in file:
            lines += [line.strip()]
    return random.choice(lines)


def func_year() -> int:
    """генерирует год"""
    return random.randint(1700, 2021)


def func_pages() -> int:
    """генерирует кол-во страниц"""
    return random.randint(0, 1500)


def func_isbn13() -> str:
    """генерирует международный стандартный книжный номер"""
    fake = Faker()
    return fake.isbn13()


def func_rating() -> float:
    """генерирует рейтинг"""
    return round(random.uniform(0, 5), 3)


def func_price() -> float:
    """генерирует цену"""
    return round(random.uniform(0, 1000), 2)


def func_discount() -> int:
    """генерирует скидку"""
    return random.randint(0, 100)


def func_author() -> list:
    """генерирует список авторов, от 1 до 3 авторов"""
    fake = Faker()
    list_ = []
    for i in range(random.randint(1, 3)):
        list_ += [fake.name()]
    return list_


if __name__ == '__main__':
    main_func()
