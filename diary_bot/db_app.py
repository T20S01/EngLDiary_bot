import os
from logging import getLogger, handlers, DEBUG, INFO, Formatter
from config.sql_statements import *
import sqlite3

# ログを残すための設定
logger = getLogger('discord')
diary_logger = getLogger('diary_db')
diary_logger.setLevel(DEBUG)
handler = handlers.RotatingFileHandler(
    filename=SQL_LOG_FILE_LOCATION,
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = Formatter(
    '[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
formatter.converter = time.localtime(time.time() + 9*60*60)
handler.setFormatter(formatter)
diary_logger.addHandler(handler)
diary_logger.propagate = False

# SQLiteのdairy_databaseがなければ作成し、そのまま接続する


def connect_database(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        diary_logger.info("CONNECT")
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
        diary_logger.info("CREATE")
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
        diary_logger.info("INSERT,"+",".join(map(str, content)))
        return _cursor_lastrowid
    except sqlite3.Error as e:
        logger.error(e)
        conn.rollback()
    finally:
        cursor.close()

# 作成中
# diary_db.logファイルの一番最近のINSERTを捜す


def get_last_insert_line():
    with open(SQL_LOG_FILE_LOCATION, 'r') as f:
        lines = f.readlines()
        for line in reversed(lines):
            if 'INSERT' in line:
                return line


# dairy_databaseの一番最近のcontentを削除する


def delete_recent_content(conn):
    cursor = conn.cursor()
    cursor.execute('BEGIN')
    try:
        # "INSERT"の行を見つける
        last_insert = get_last_insert_line()
        insert_pos = last_insert.find("INSERT")
        # "INSERT"以降の文字列を取得する
        last_insert_list = last_insert[insert_pos:].split(",")
        cursor = conn.cursor()
        print(last_insert_list[1])
        cursor.execute(DELETE_RECENT_CONTENT, "".join(last_insert_list[1]))
        diary_logger.info("DELETE")
        return last_insert_list
    except sqlite3.Error as e:
        logger.error(e)
        conn.rollback()
        return None
    finally:
        cursor.close()


# SQLiteでSELECT文を実行する基を作る
def exeute_select_in_dairy_dababase(conn, TEM_QUERY, TEM_ARGUMENT=None):
    cursor = conn.cursor()
    _corsor_fetchall = None
    try:
        if TEM_ARGUMENT == None:
            cursor.execute(TEM_QUERY)
            _corsor_fetchall = cursor.fetchall()
            diary_logger.info("SELECT")
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
