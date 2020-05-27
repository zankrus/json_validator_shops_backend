"""Файл для работы с JSON, тут хранится схема , функции."""

import jsonschema
from jsonschema import validate
import random
import json

SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "id": 123,
            "name": "Телевизор",
            "package_params": {
                "width": 5,
                "height": 10
            },
            "location_and_quantity": [
                {
                    "location": "Магазин на Ленина",
                    "amount": 7
                },
                {
                    "location": "Магазин в центре",
                    "amount": 3
                }
            ]
        }
    ],
    "required": [
        "id",
        "name",
        "package_params",
        "location_and_quantity"
    ],
    "additionalProperties": False,
    "properties": {
        "id": {
            "$id": "#/properties/id",
            "type": "integer",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                123
            ]
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Телевизор"
            ]
        },
        "package_params": {
            "$id": "#/properties/package_params",
            "type": "object",
            "title": "The package_params schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "width": 5,
                    "height": 10
                }
            ],
            "required": [
                "width",
                "height"
            ],
            "additionalProperties": True,
            "properties": {
                "width": {
                    "$id": "#/properties/package_params/properties/width",
                    "type": "integer",
                    "title": "The width schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        5
                    ]
                },
                "height": {
                    "$id": "#/properties/package_params/properties/height",
                    "type": "integer",
                    "title": "The height schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        10
                    ]
                }
            }
        },
        "location_and_quantity": {
            "$id": "#/properties/location_and_quantity",
            "type": "array",
            "title": "The location_and_quantity schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "location": "Магазин на Ленина",
                        "amount": 7
                    },
                    {
                        "location": "Магазин в центре",
                        "amount": 3
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/location_and_quantity/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "location": "Магазин на Ленина",
                                "amount": 7
                            }
                        ],
                        "required": [
                            "location",
                            "amount"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "location": {
                                "$id": "#/properties/location_and_quantity/items/anyOf/0/properties/location",
                                "type": "string",
                                "title": "The location schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "Магазин на Ленина"
                                ]
                            },
                            "amount": {
                                "$id": "#/properties/location_and_quantity/items/anyOf/0/properties/amount",
                                "type": "integer",
                                "title": "The amount schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    7
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/location_and_quantity/items"
            }
        }
    }
}

goods_id_and_names = {1: "Телевизор", 2: 'Смартфон', 3: "Ноутбук", 4: "Собака"}


def json_messager() -> dict:
    """Тестовая функция-генерирует тестовые JSON, как валидный так и нет."""
    random_event = random.randint(2, 4)
    if random_event > 1:
        jeson_valid = {
            "id": random.randint(1, 4),
            "name": goods_id_and_names[random.randint(1, 4)],
            "package_params": {
                "width": random.randint(1, 10),
                "height": random.randint(1, 10)
            },
            "location_and_quantity": [
                {
                    "location": "Магазин на Ленина",
                    "amount": random.randint(0, 10)
                },
                {
                    "location": "Магазин в центре",
                    "amount": random.randint(0, 10)
                },
                {
                    "location": "Магазин в Далеке",
                    "amount": random.randint(0, 10)
                }
            ]
        }
        return jeson_valid
    else:
        jeson_invalid = {
            "id": random.randint(1, 10),
            "name": random.randint(1, 10),
            "package_params": {
                "width": random.randint(1, 10),
                "height": random.randint(1, 10)
            },
            "location_and_quantity": [
                {
                    "location": "Магазин на Ленина",
                    "amount": random.randint(0, 10)
                },
                {
                    "location": "Магазин в центре",
                    "amount": random.randint(0, 10)
                }
            ]
        }
        return jeson_invalid


def validator(json: dict, schema: dict = SCHEMA) -> any:
    """Валидатор JSON."""
    try:
        validate(json, schema)
        return json
    except jsonschema.exceptions.ValidationError:
        return 'Невалидный json'


def handler(json: dict) -> Generator[dict] :
    """Обработчик входящих JSON, возвращается генератор словарей из входящей JSON."""
    final_dict = []
    example_dict = []
    for key in json:
        try:
            a = key, json[key]
            if isinstance(json[key], dict):
                for inner_key in json[key]:
                    b = inner_key, json[key][inner_key]
                    example_dict.append(b)
            if isinstance(json[key], list):
                for list_key in json[key]:
                    counter = 0
                    d = example_dict[::]
                    for inner_list_key in list_key:
                        c = inner_list_key, list_key[inner_list_key]
                        d.append(c)
                        counter += 1
                        if counter % 2 == 0:
                            final_dict.append(d)
            elif key != "package_params":
                example_dict.append(a)
        except TypeError:
            pass
        for i in range(len(final_dict)):
            yield dict(final_dict[i])


def file_jsoner(incom_json: dict) -> dict:
    """Функция создания файла с JSON."""
    with open('test.json', 'w') as j:
        json.dump(incom_json, j, ensure_ascii=False)
    with open('test.json') as j:
        a = json.loads(j.read())
        return a
