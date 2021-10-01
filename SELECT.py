import sqlalchemy
import json
import os
from settings import *
from pprint import pprint


def read_json(path_: str):
    with open(path_, encoding='utf-8') as f:
        return json.load(f)


auth = read_json('authenticator.json')

# создаем engine
engine = sqlalchemy.create_engine(f"postgresql://{auth['user']}:{auth['password']}@localhost:5432/{auth['database']}")
con = engine.connect()

# # Запросы
#
# print('1. Название и год выхода альбомов, вышедших в 2018 году')
# res = con.execute("""SELECT name, year_of_release FROM album
#                      WHERE year_of_release = 2018;
#                   """).fetchall()
# pprint(res)
# print('\n'*2)
#
# print('2. Название и продолжительность самого длительного трека')
# res = con.execute("""SELECT name, duration FROM track
#                      ORDER BY duration DESC
#                      LIMIT 1;
#                   """).fetchall()
# pprint(res)
# print('\n'*2)
#
# print('3. Название треков, продолжительность которых не менее 3,5 минуты')
# res = con.execute("""SELECT name FROM track
#                      WHERE duration >= 3.5*60*1000;
#                   """).fetchall()
# pprint(res)
# print('\n'*2)
#
# print('4. Названия сборников, вышедших в период с 2018 по 2020 год включительно')
# res = con.execute("""SELECT name FROM album
#                      WHERE year_of_release BETWEEN 2018 AND 2020;
#                   """).fetchall()
# pprint(res)
# print('\n'*2)
#
# print('5. Исполнители, чье имя состоит из 1 слова')
# res = con.execute("""SELECT name FROM executor
#                      WHERE name not LIKE '%% %%';
#                   """).fetchall()
# pprint(res)
# print('\n'*2)

print('6. Название треков, которые содержат слово "мой"/"my"')
res = con.execute("""SELECT name FROM track
                     WHERE name iLIKE '%%мой%%' or name iLIKE '%%my%%';
                  """).fetchall()
pprint(res)



