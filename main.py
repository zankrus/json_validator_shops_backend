from homework.data_base import data_base_creating, insert_goods , insert_shops_goods
from homework.jsoner import validator, json_messager, handler

if __name__ == '__main__':
    data_base_creating()
    jsonka = validator(json_messager())
    print('Поступившая JSON: ')
    print(jsonka)
    print('')

    zapros = handler(jsonka)

    for element in zapros:
        print(element)
        insert_goods(element)
        insert_shops_goods(element)




