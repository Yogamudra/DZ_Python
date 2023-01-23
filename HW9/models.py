# Прикрутить бота к задаче о телефонном справочнике.
# Бот должен показать весь телефонный справочник, найти по фамилии,
# а также предоставить возможность добавлять и удалять записи в справочнике.
# Проект выложить на гитхаб, добавить файл requirements.txt,
# в котором указать необходимые библиотеки для установки.
# Папку venv загружать на гитхаб не нужно!



# https://habr.com/ru/post/321510/

import sqlite3

def get_contacts(cursor):
    '''показать все контакты'''
    cursor.execute("select * from phone")
    results = cursor.fetchall()
    return results


def get_contact(item, cursor):
    '''поиск записи'''
    cursor.execute(f"select * from phone where surname like '%{item}%'"
                   f"or name like '%{item}%'")
    results = cursor.fetchall()
    if results:
        return results
    return 'Контакт не найден'


def add_contact(data, conn, cursor):
    '''добавить контакт'''
    name, surname, telephone = data
    cursor.execute(
        f"insert into phone (name, surname, telephone, description) "
        f"values ('{name}', '{surname}', {telephone}, '')")
    conn.commit()


def delete(id, conn, cursor):
    '''Удалить контакт'''
    try:
        cursor.execute(
            f"delete from phone where id={id}"
        )
        conn.commit()
        return 'Контакт был успешно удален'
    except:
        return 'Контакт не найден. Попробуйте еще раз'
