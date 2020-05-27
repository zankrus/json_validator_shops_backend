"""Этот файл отвечает за работу БД. Используемая БД - Postgres."""
import psycopg2

con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="221052",
    host="127.0.0.1",
    port="5432"
)


def data_base_creating() -> None:
    """Функция создает таблицы GOODS и SHOPS_GOOD,если они не созданы."""
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS GOODS
         (ID SERIAL  PRIMARY KEY NOT NULL ,
         NAME VARCHAR NOT NULL,
         PACKAGE_HEIGHT FLOAT NOT NULL,
         PACKAGE_WIDTH FLOAT NOT NULL);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS SHOPS_GOODS
         (ID SERIAL  PRIMARY KEY NOT NULL ,
         ID_GOOD INT NOT NULL,
         LOCATION VARCHAR NOT NULL,
         AMOUTH INT NOT NULL,
         FOREIGN KEY (ID_GOOD)  REFERENCES GOODS (ID));''')

    con.commit()


def insert_goods(a: dict) -> None:
    """Функция вставляет значения в таблицу GOODS или обновляет их, если они уже вставлены."""
    a = a
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO GOODS (ID,NAME,PACKAGE_HEIGHT,PACKAGE_WIDTH) VALUES (%s, %s, %s, %s);",
            (a['id'], a['name'], a['height'], a['width'])
        )

        con.commit()
    except psycopg2.errors.UniqueViolation:
        cur.execute("ROLLBACK")
        con.commit()
        cur.execute(
            "UPDATE GOODS SET NAME = %s ,PACKAGE_HEIGHT = %s, PACKAGE_WIDTH = %s WHERE ID = %s",
            (a['name'], a['height'], a['width'], a['id'])
        )
        con.commit()


def insert_shops_goods(a: dict) -> None:
    """Функция вставляет значения в таблицу SHOPS_GOODS, или обновляет их."""
    b = select()
    a = a
    cur = con.cursor()
    if (a['id'], a['location']) in b:
        cur.execute(
            "UPDATE SHOPS_GOODS SET AMOUTH = %s  WHERE LOCATION = %s AND ID_GOOD = %s",
            (a['amount'], a['location'], a['id'])
        )
        con.commit()
    else:
        cur.execute(
            "INSERT INTO SHOPS_GOODS (ID,ID_GOOD,LOCATION,AMOUTH) VALUES (default,%s, %s, %s)",
            (a['id'], a['location'], a['amount'])
        )
        con.commit()


def select() -> list:
    """Вспомоготельная функция , нужная для проверки  вставленных значений в SHOPS_GOODS.radon mi -m ."""
    cur = con.cursor()
    cur.execute("SELECT  ID_GOOD,LOCATION from SHOPS_GOODS")
    rows = cur.fetchall()
    flag = []

    for row in rows:
        flag.append((row[0], row[1]))

    return flag
