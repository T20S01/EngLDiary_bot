SQL_LOG_FILE_LOCATION =  "./database/db_sql.log"

CREATE_TABLE_IN_DIARY_DATABASE = """
    CREATE TABLE IF NOT EXISTS contents (
    id INTEGER PRIMARY KEY, 
    user TEXT NOT NULL, 
    message TEXT NOT NULL,
    create_at DATETIME NOT NULL,
    channel TEXT NOT NULL,
    guild TEXT NOT NULL,
    image_url TEXT
    );
    """

INSERT_CONTENT = "INSERT INTO contents(id,user,message,create_at,channel,guild,image_url)VALUES(?,?,?,?,?,?,?)"
DELETE_RECENT_CONTENT = "DELETE FROM contents WHERE id = ?"


SELECT_ALL_CONTENT = "SELECT * FROM contents"
SELECT_ALL_MESSAGE = "SELECT message FROM contents"
SELECT_ALL_MESSAGE_CREATE_AT = "SELECT message, create_at FROM contents"
SELECT_ALL_LIKE_WORD = "SELECT * FROM contents WHERE message LIKE ?"
SELECT_ALL_WHERE_DATE = "SELECT * FROM contents WHERE DATE(create_at) = ?"
