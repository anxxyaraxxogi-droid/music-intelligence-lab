import csv
from analysis import analyze_playlist
# from database import create_connection, create_tables
from database import (
    create_connection,
    create_tables,
    insert_songs,
    get_genre_counts
)

connection = create_connection()


create_tables(connection)


 
songs = []

with open("../data/songs.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        songs.append(row)

insert_songs(connection, songs)

genre_counts = get_genre_counts(connection)

print("Genre counts:", genre_counts)
 
results = analyze_playlist(songs)

print(results)