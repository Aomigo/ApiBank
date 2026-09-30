import sqlite3
from pathlib import Path #for system calls and path manipulations   

DB_PATH = Path(__file__).parent / "apibank.db"


def get_db_connection() -> sqlite3.Connection:
    # Connexion to the SQLite database and enable foreign key support
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
