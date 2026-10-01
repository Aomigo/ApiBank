import sqlite3
from account import Account
from pathlib import Path #for system calls and path manipulations   

DB_PATH = Path(__file__).parent / "apibank.db"


def get_db_connection() -> sqlite3.Connection:
    # Connexion to the SQLite database and enable foreign key support
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn



def get_account_bdd(id: str) -> Account:
    conn = get_db_connection()
    row = conn.execute("SELECT id, pseudo, balance FROM account WHERE id = ?", (id,)).fetchone()
    conn.close()
    return Account(row["pseudo"], str(row["id"]), row["balance"])

def get_save_account(account: Account):
    conn = get_db_connection()
    acc_id = account.id[0] 
    conn.execute("UPDATE account SET balance = ? WHERE id = ?", (account.balance.balance, acc_id))
    conn.commit()
    conn.close()
    
#idée pour le cas de make_deposit et make_transaction : 
#faire dans le fichier database.py  (vu que c'est le fichier de connexion bdd)(ou autre si on crée un dossier " connexion database") : 
#=> Des fonctions pour le lien avec la table account et la save transaction
#BUT :  ne plus utiliser l'interface RepositoryAccount dans  make_deposit et make_transaction => Use BDD