def clear_songs(connection):
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM songs
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

    connection.commit()

def get_all_songs(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM songs
    """)

    songs = cursor.fetchall()

    return songs


def get_genre_counts(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT genre, COUNT(*)
        FROM songs
        GROUP BY genre
        ORDER BY COUNT(*) DESC
    """)

    genre_counts = cursor.fetchall()

    return genre_counts


def get_artist_counts(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT artist, COUNT(*)
        FROM songs
        GROUP BY artist
        ORDER BY COUNT(*) DESC
    """)

    artist_counts = cursor.fetchall()

    return artist_counts


def get_average_rating(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT AVG(rating)
        FROM songs
    """)

    average_rating = cursor.fetchone()[0]

    return average_rating


def get_oldest_song(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT song, artist, year
        FROM songs
        ORDER BY year ASC
        LIMIT 1
    """)

    oldest_song = cursor.fetchone()

    return oldest_song


def get_newest_song(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT song, artist, year
        FROM songs
        ORDER BY year DESC
        LIMIT 1
    """)

    newest_song = cursor.fetchone()

    return newest_song


def get_top_rated_songs(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT song, artist, rating
        FROM songs
        ORDER BY rating DESC
        LIMIT 5
    """)

    top_songs = cursor.fetchall()

    return top_songs