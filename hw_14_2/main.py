# 2024/01/23 00:00|Создание, Изменение и Удаление элементов

import sqlite3

DATABASE = 'my_bd.db'


def init_data_base(database):
    # Инициализация бд
    with sqlite3.connect(database) as con_db:
        cur = con_db.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
        )''')
        con_db.commit()


def add_elem_db(cur, username, email, age, balance):
    cur.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                (username, email, age, balance))


def add_data():
    with sqlite3.connect(DATABASE) as con_db:
        cur = con_db.cursor()
        for i in range(10):
            add_elem_db(cur, f'username{i + 1}', f'email{i + 1}@email.ru',
                        (i + 1) * 10, 1000)
        con_db.commit()


def update_balance_db(cur, balance, username):
    cur.execute("UPDATE Users SET balance = ? WHERE username = ?",
                    (balance, username))


def change_balance(new_balance):
    with sqlite3.connect(DATABASE) as con_db:
        cur = con_db.cursor()
        cur.execute("SELECT id, username FROM Users WHERE id % 2 <> 0")
        for user in cur.fetchall():
            update_balance_db(cur, new_balance, username=user[1])
        con_db.commit()


def del_elem_db(cur, username):
    cur.execute("DELETE FROM Users WHERE username = ?", (username, ))


def remove_users():
    with sqlite3.connect(DATABASE) as con_db:
        cur = con_db.cursor()
        cur.execute("SELECT id, username FROM Users WHERE (id % 3 = 1) OR (id = 1)")
        for user in cur.fetchall():
            del_elem_db(cur, username=user[1])
        con_db.commit()


def get_age(age):
    with sqlite3.connect(DATABASE) as con_db:
        cur = con_db.cursor()
        cur.execute(f"SELECT age, username, email, age, balance FROM Users WHERE age <> {age}")
        for user in cur.fetchall():
            print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')
        con_db.commit()


def remove_id_bd(user_id):
    with sqlite3.connect(DATABASE) as con_bd:
        cur = con_bd.cursor()
        cur.execute(f'DELETE FROM Users WHERE id = {user_id}')
        con_bd.commit()


def count_bd(database):
    counts = 0
    with sqlite3.connect(database) as con_db:
        cur = con_db.cursor()
        cur.execute('SELECT COUNT(*) FROM Users')
        counts = cur.fetchone()[0]
        con_db.commit()
    return counts


def sum_balance_bd(database):
    balance = 0
    with sqlite3.connect(database) as con_db:
        cur = con_db.cursor()
        cur.execute('SELECT SUM(balance) FROM Users')
        balance = cur.fetchone()[0]
        con_db.commit()
    return balance


def avg_balance_bd(database):
    avg_balance = 0
    with sqlite3.connect(database) as con_db:
        cur = con_db.cursor()
        cur.execute('SELECT AVG(balance) FROM Users')
        avg_balance = cur.fetchone()[0]
        con_db.commit()
    return avg_balance


if __name__ == '__main__':
    init_data_base(DATABASE)

    # add_data()
    # change_balance(500)
    # remove_users()
    # get_age(age=60)
    remove_id_bd(user_id=6)
    print(count_bd(DATABASE))
    print(sum_balance_bd(DATABASE))
    print(avg_balance_bd(DATABASE))
