"""Основной файл для работы. Запусукать его."""
from data_base import data_base_creating, insert_goods, insert_shops_goods
from jsoner import validator, json_messager, handler, file_jsoner

if __name__ == '__main__':
    file_json = file_jsoner(json_messager())
    data_base_creating()
    jsonka = validator(file_json)
    print('Поступившая JSON: ')
    print(jsonka)
    print('')

    zapros = handler(jsonka)

    for element in zapros:

        insert_goods(element)
        insert_shops_goods(element)
