
from app.services.data_service import load_dataset
from app.services.analysis_service import analyze_playlist
from app.database.connection import create_connection
from app.database.models import create_tables
from app.database.queries import (
    clear_songs,
    insert_songs,
    get_all_songs,
    get_genre_counts,
    get_average_rating,
    get_artist_counts,
    get_oldest_song,
    get_newest_song,
    get_top_rated_songs
)

connection = create_connection()


create_tables(connection)


 
songs = []
df = load_dataset("../data/seed/songs.csv")

songs = df.to_dict("records")
# with open("../data/seed/songs.csv", "r") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         songs.append(row)
clear_songs(connection)
insert_songs(connection, songs)

genre_counts = get_genre_counts(connection)

print("Genre counts:", genre_counts)

genre_counts = get_genre_counts(connection)
print("Genre counts:", genre_counts)

average_rating = get_average_rating(connection)
print("Average rating:", average_rating)

artist_counts = get_artist_counts(connection)

print("Artist counts:")

for artist, count in artist_counts:
    print(f"{artist}: {count}")


oldest_song = get_oldest_song(connection)

print("Oldest song:", oldest_song)

newest_song = get_newest_song(connection)
print("Newest song:", newest_song)

top_songs = get_top_rated_songs(connection)

print("\nTop rated songs:")

for song, artist, rating in top_songs:
    print(f"{song} - {artist} ({rating})")

results = analyze_playlist(df)

print(results)