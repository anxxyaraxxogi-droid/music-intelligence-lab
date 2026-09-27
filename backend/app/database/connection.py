import sqlite3


def create_connection():
    connection = sqlite3.connect("../database/music.db")
    return connection