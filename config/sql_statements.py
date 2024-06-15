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
INSERT_CONTENT = """
    INSERT INTO contents(id,user,message,create_at,channel,guild,image_url)VALUES(?,?,?,?,?,?,?)
    """
