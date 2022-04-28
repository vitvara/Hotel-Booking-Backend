import sqlite3
import pandas as pd
from sqlite3 import Error
import os
import sys

XL_HOTEL_FILE_PATH = os.path.join("data", 'room.xlsx')
XL_USERS_FILE_PATH = os.path.join("data", "users.xlsx")


def connect_to_db(db_file):
    sqlite3_conn = None
    try:
        sqlite3_conn = sqlite3.connect(db_file)
        return sqlite3_conn

    except Error as err:
        print(err)

        if sqlite3_conn is not None:
            sqlite3_conn.close()


def insert_hotel_values_to_table(xl_file, database_url, selected=True):
    conn = connect_to_db(database_url)
    if conn is not None:
        c = conn.cursor()

        # Create table if it is not exist
        c.execute(f"""CREATE TABLE IF NOT EXISTS room(
    id              INTEGER PRIMARY KEY,
    room_number     INTEGER NOT NULL,
    building        TEXT NOT NULL,
    floor           INTEGER NOT NULL,
    bed             INTEGER,
    max_guest       INTEGER,
    price          INTEGER,
    status          TEXT DEFAULT 'avaliable',
    type            TEXT,
    user_id         INTEGER DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);""")
        print("[ROOM] SQL create table Finish")
        if selected:
            df = pd.read_excel(xl_file)
            df.to_sql(name='room', con=conn, if_exists='append', index=False)
            conn.close()
            print('[ROOM] SQL insert process finished')
    else:
        print('[ROOM] Connection to database failed')


def insert_user_values_to_table(xl_file, database_url, selected=True):
    conn = connect_to_db(database_url)
    if conn is not None:
        c = conn.cursor()

        # Create table if it is not exist
        c.execute(f"""CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT    NOT NULL,
    password         TEXT    NOT NULL
);""")
        print("[USER] SQL create table Finish")
        if selected:
            df = pd.read_excel(xl_file)
            df.to_sql(name='users', con=conn, if_exists='append', index=False)
            conn.close()
            print('[USER] SQL insert process finished')
    else:
        print('[USER] Connection to database failed')


if __name__ == '__main__':
    try:
        database_url = sys.argv[1]
        file = open('.env', 'w')
        file.write(f"DB_URL={database_url}")
        file.close()
        print("Created .env file")
        insert_user_values_to_table(XL_USERS_FILE_PATH, database_url)
        insert_hotel_values_to_table(XL_HOTEL_FILE_PATH, database_url)
    except IndexError:
        print("Database URL required.")
