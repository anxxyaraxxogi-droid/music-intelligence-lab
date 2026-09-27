def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            song TEXT,
            artist TEXT,
            genre TEXT,
            year INTEGER,
            rating REAL
        )
    """)

    connection.commit()