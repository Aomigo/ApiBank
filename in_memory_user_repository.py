from user import User
from user_repository_interface import UserRepository
from database import get_db_connection


class _UserDict:
    def __getitem__(self, id: str):
        return Users().getById(id)


class Users(UserRepository):
    users = _UserDict()

    def getById(self, id: str) -> User:
        conn = get_db_connection()
        row = conn.execute("SELECT id, pseudo, email, mdp FROM user WHERE id = ?", (id,)).fetchone()
        conn.close()
        if not row:
            return None
        return User(str(row["id"]), row["pseudo"], row["email"], row["mdp"])

    def save(self, user: User):
        conn = get_db_connection()
        row = conn.execute("SELECT id FROM user WHERE id = ?", (user.id,)).fetchone()
        if row:
            conn.execute(
                "UPDATE user SET pseudo = ?, email = ?, mdp = ? WHERE id = ?",
                (user.username, user.email, user.password, user.id)
            )
        else:
            cursor = conn.execute(
                "INSERT INTO user (pseudo, email, mdp) VALUES (?, ?, ?)",
                (user.username, user.email, user.password)
            )
            user.id = str(cursor.lastrowid)
        conn.commit()
        conn.close()
        return user

    def create_account(self, user_id: str, name: str):
        conn = get_db_connection()
        cursor = conn.execute(""" INSERT INTO account (pseudo, balance, uuid) VALUES (?,?,?)""",(name, 0, user_id))
        account_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return account_id
