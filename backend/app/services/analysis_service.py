import pandas as pd


def analyze_playlist(df):

    # BASIC ANALYSIS

    song_count = len(df)

    artist_count = df["artist"].nunique()

    genre_count = df["genre"].nunique()


    # GENRE ANALYSIS

    genre_counts = df["genre"].value_counts()

    most_common_genre = genre_counts.index[0]

    max_genre_count = genre_counts.iloc[0]

    max_genre_percentage = (max_genre_count / song_count) * 100


    # ARTIST ANALYSIS

    artist_counts = df["artist"].value_counts()

    most_common_artist = artist_counts.index[0]

    max_artist_count = artist_counts.iloc[0]

    max_artist_percentage = (max_artist_count / song_count) * 100


    # YEAR ANALYSIS

    oldest_year = df["year"].min()

    year_counts = df["year"].value_counts().sort_index()

    return {
        "song_count": song_count,
        "artist_count": artist_count,
        "genre_count": genre_count,
        "genre_counts": genre_counts.to_dict(),
        "most_common_genre": most_common_genre,
        "genre_percentage": max_genre_percentage,
        "artist_counts": artist_counts.to_dict(),
        "most_common_artist": most_common_artist,
        "artist_percentage": max_artist_percentage,
        "oldest_year": oldest_year,
        "year_counts": year_counts.to_dict()
    }