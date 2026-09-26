import sqlite3


def create_connection():
    connection = sqlite3.connect("../database/music.db")
    return connection


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

def insert_songs(connection, songs):
    cursor = connection.cursor()

    for song in songs:
        cursor.execute("""
            INSERT INTO songs (song, artist, genre, year, rating)
            VALUES (?, ?, ?, ?, ?)
        """, (
            song["Song"],
            song["artist"],
            song["genre"],
            int(song["year"]),
            float(song["rating"])
        ))

def get_all_songs(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM songs")

    songs = cursor.fetchall()

    return songs

def get_genre_counts(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT genre, COUNT(*)
        FROM songs
        GROUP BY genre
    """)

    genre_counts = cursor.fetchall()

    return genre_counts
    

    