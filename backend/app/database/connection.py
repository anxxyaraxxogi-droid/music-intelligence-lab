import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]
DATABASE_PATH = BASE_DIR / "database" / "music.db"


def create_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection