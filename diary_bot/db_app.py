from logging import getLogger
from config.sql_statements import *
import sqlite3

# ログを残すための設定
logger = getLogger('discord')

# SQLiteのdairy_databaseがなければ作成し、そのまま接続する
def connect_database(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        logger.error(e)
    return conn

# SQLiteのdairy_databaseにdairy_tableがなければ作成し、そのまま接続する
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('BEGIN')
    try:
        cursor.execute(CREATE_TABLE_IN_DIARY_DATABASE)
        conn.commit()
    except sqlite3.Error as e:
        logger.error(e)
        conn.rollback()
    finally:
        cursor.close()

# SQLiteのdairy_databaseにcontentを追加する
def add_content(conn, content):
    _cursor_lastrowid = None
    cursor = conn.cursor()
    cursor.execute('BEGIN')
    try:
        cursor.execute(INSERT_CONTENT, content)
        conn.commit()
        _cursor_lastrowid = cursor.lastrowid
        return _cursor_lastrowid
    except sqlite3.Error as e:
        logger.error(e)
        conn.rollback()
    finally:
        cursor.close()

# 作成中

# SQLiteのdairy_databaseにcontentを追加する
# def delete_recent_content(conn):
#     cursor = conn.cursor()
#     cursor.execute('BEGIN')
#     try:
#         cursor = conn.cursor()
#         cursor.execute('BEGIN')
#     except sqlite3.Error as e:
#         logger.error(e)
#         conn.rollback()
#     finally:
#         cursor.close()


# SQLiteでSELECT文を実行する基を作る
def exeute_select_in_dairy_dababase(conn, TEM_QUERY, TEM_ARGUMENT=None):
    cursor = conn.cursor()
    _corsor_fetchall = None
    try:
        if TEM_ARGUMENT == None:
            cursor.execute(TEM_QUERY)
            _corsor_fetchall = cursor.fetchall()
        else:
            cursor.execute(TEM_QUERY, TEM_ARGUMENT)
            _corsor_fetchall = cursor.fetchall()
        return _corsor_fetchall
    except sqlite3.Error as e:
        logger.error(e)
        conn.rollback()
    finally:
        cursor.close()

# SQLiteのdairy_databaseからすべての要素をselectする
def select_all_contents(conn):
    return exeute_select_in_dairy_dababase(
        conn,
        SELECT_ALL_CONTENT
    )

# SQLiteのdairy_databaseからmessage列のすべての要素をselectする
def select_all_messages(conn):
    return exeute_select_in_dairy_dababase(
        conn,
        SELECT_ALL_MESSAGE
    )

# SQLiteのdairy_databaseからmessage, create_at列のすべての要素をselectする
def select_all_messages_create_at(conn):
    return exeute_select_in_dairy_dababase(
        conn,
        SELECT_ALL_MESSAGE_CREATE_AT
    )


# SQLiteのdairy_databaseからfind_lettersがmessagegに含まれるすべての要素をselectする
def select_all_like_letters(conn, find_letters: str):
    return exeute_select_in_dairy_dababase(
        conn,
        SELECT_ALL_LIKE_WORD,
        ('%'+find_letters+'%',)
    )

# SQLiteのdairy_databaseからfind_wordがmessagegに含まれるすべての要素をselectする
def select_all_like_word(conn, find_word: str):
    return exeute_select_in_dairy_dababase(
        conn,
        SELECT_ALL_LIKE_WORD,
        ('% '+find_word+' %',)
    )

# SQLiteのdairy_databaseからfind_dateがcreate_atに含まれるすべての要素をselectする
def select_all_where_date(conn, find_date: str):
    return exeute_select_in_dairy_dababase(
        conn,
        SELECT_ALL_WHERE_DATE,
        (find_date,)
    )
