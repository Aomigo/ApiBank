import sqlite3
from pathlib import Path #for system calls and path manipulations   



DB_PATH = Path(__file__).parent / "apibank.db"
SQL_PATH = Path(__file__).parent / "data.sql"

#generate the .db file and initialize the database with the schema and data defined in the SQL script
#.db file will be created if it does not exist

def init_db():
    conn = sqlite3.connect(DB_PATH)
    with open(SQL_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.close()
    print("Database apibank.db initialisée avec succès.")

if __name__ == "__main__":
    init_db()

#   => python init_db.py to generate .db

