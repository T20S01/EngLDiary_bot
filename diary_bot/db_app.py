from config import sql_statements

import sqlite3


def connect_database(db_file):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_statements.CREATE_TABLE_IN_DIARY_DATABASE)
    except sqlite3.Error as e:
        print(e)


def add_content(conn, content):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_statements.INSERT_CONTENT, content)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return cursor.lastrowid


def select_contents(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contents')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def select_message(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contents')
    rows = cursor.fetchall()
    for row in rows:
        print(row)