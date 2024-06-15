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

SELECT_ALL_CONTENT = "SELECT * FROM contents"
SELECT_ALL_MESSAGE = "SELECT message FROM contents"
SELECT_ALL_LIKE_WORD = "SELECT * FROM contents WHERE message LIKE ?"
SELECT_ALL_WHERE_DATE = "SELECT * FROM contents WHERE DATE(create_at) = ?"
SELECT_ALL_BETWEEN_TIME_SAME_DAY = "SELECT * FROM contents WHERE TIME(create_at) >= ? AND TIME(create_at) <= ?"
SELECT_ALL_BETWEEN_TIME_DIFFERENT_DAYS = """
    SELECT * FROM contents
    WHERE (TIME(create_at) >= ? AND TIME(create_at) <= '23:59')
    OR (TIME(create_at) >= '00:00' AND TIME(create_at) <= ?)
    """