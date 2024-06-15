from config import sql_statements

import sqlite3

# SQLiteのdbがなければ作成し、そのまま接続する


def connect_database(db_file):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    return conn

# SQLiteのdairy_databaseがなければ作成し、そのまま接続する


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_statements.CREATE_TABLE_IN_DIARY_DATABASE)
    except sqlite3.Error as e:
        print(e)

# SQLiteのdairy_databaseにcontentを追加する


def add_content(conn, content):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_statements.INSERT_CONTENT, content)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return cursor.lastrowid

# SQLiteでSELECT文を実行する基を作る


def exeute_select_in_dairy_dababase(conn, TEM_QUERY, TEM_ARGUMENT=None):
    try:
        cursor = conn.cursor()
        if TEM_ARGUMENT is None:
            cursor.execute(TEM_QUERY)
        else:
            cursor.execute(TEM_QUERY, TEM_ARGUMENT)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
        return None

# SQLiteのdairy_databaseからすべての要素をselectする


def select_all_contents(conn):
    return exeute_select_in_dairy_dababase(
        conn,
        sql_statements.SELECT_ALL_CONTENT
    )

# SQLiteのdairy_databaseからmessage列のすべての要素をselectする


def select_all_messages(conn):
    return exeute_select_in_dairy_dababase(
        conn,
        sql_statements.SELECT_ALL_MESSAGE
    )


# SQLiteのdairy_databaseからfind_lettersがmessagegに含まれるすべての要素をselectする
def select_all_like_letters(conn, find_letters: str):
    return exeute_select_in_dairy_dababase(
        conn,
        sql_statements.SELECT_ALL_LIKE_WORD,
        ('%'+find_letters+'%',)
    )


# SQLiteのdairy_databaseからfind_wordがmessagegに含まれるすべての要素をselectする
def select_all_like_word(conn, find_word: str):
    return exeute_select_in_dairy_dababase(
        conn,
        sql_statements.SELECT_ALL_LIKE_WORD,
        ('% '+find_word+' %',)
    )

# SQLiteのdairy_databaseからfind_dateがcreate_atに含まれるすべての要素をselectする


def select_all_where_date(conn, find_date: str):
    return exeute_select_in_dairy_dababase(
        conn,
        sql_statements.SELECT_ALL_WHERE_DATE,
        (find_date,)
    )

# SQLiteのdairy_databaseからfind_time内にcreate_atが含まれるすべての要素をselectする
# ただし、時間が日を跨ぐ場合とそうでない場合は別の関数を呼び出す

def select_all_where_time_same_day(conn, find_time: tuple):
    return exeute_select_in_dairy_dababase(
        conn,
        sql_statements.SELECT_ALL_BETWEEN_TIME_SAME_DAY,
        find_time
    )

def select_all_where_time_different_day(conn, find_time: tuple):
    return exeute_select_in_dairy_dababase(
        conn,
        sql_statements.SELECT_ALL_BETWEEN_TIME_DIFFERENT_DAYS,
        find_time
    )