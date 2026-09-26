def analyze_playlist(songs):
    song_count = len(songs)

    # Count unique artists
    artists = []

    for song in songs:
        artists.append(song["artist"])

    unique_artists = set(artists)
    artist_count = len(unique_artists)

    # Count unique genres
    genres = []

    for song in songs:
        genres.append(song["genre"])

    unique_genres = set(genres)
    genre_count = len(unique_genres)

    # Count how many songs belong to each genre
    genre_counts = {}

    for genre in genres:
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

    # Find most common genre
    max_count = 0
    max_genre = ""
    max_genre_percentage = 0.0

    for genre in genre_counts:
        if genre_counts[genre] > max_count:
            max_count = genre_counts[genre]
            max_genre = genre
            max_genre_percentage = (max_count / song_count) * 100

    # Count how many songs belong to each artist
    artist_counts = {}

    for artist in artists:
        if artist in artist_counts:
            artist_counts[artist] += 1
        else:
            artist_counts[artist] = 1

    # Find most common artist
    max_artist_count = 0
    max_artist = ""
    max_artist_percentage = 0.0

    for artist in artist_counts:
        if artist_counts[artist] > max_artist_count:
            max_artist_count = artist_counts[artist]
            max_artist = artist
            max_artist_percentage = (max_artist_count / song_count) * 100

    # Find oldest song
    years = []

    for song in songs:
        years.append(int(song["year"]))

    oldest_year = min(years)

    return {
        "song_count": song_count,
        "artist_count": artist_count,
        "genre_count": genre_count,
        "genre_counts": genre_counts,
        "most_common_genre": max_genre,
        "genre_percentage": max_genre_percentage,
        "artist_counts": artist_counts,
        "most_common_artist": max_artist,
        "artist_percentage": max_artist_percentage,
        "oldest_year": oldest_year
    }