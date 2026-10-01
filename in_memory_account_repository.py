from account import Account
from repository_interface import AccountRepository
from database import get_db_connection


class _AccountDict:
    def __getitem__(self, id: str):
        return Accounts().getById(id)


class Accounts(AccountRepository):
    accounts = _AccountDict()

    def getById(self, id: str) -> Account:
        conn = get_db_connection()
        row = conn.execute(
            "SELECT id, pseudo, balance FROM account WHERE id = ? OR uuid = ?",
            (str(id), str(id))
        ).fetchone()
        conn.close()
        if not row:
            return None
        return Account(row["pseudo"], str(row["id"]), row["balance"])

    def save(self, account: Account):
        conn = get_db_connection()
        conn.execute(
            "UPDATE account SET balance = ? WHERE id = ? OR uuid = ?",
            (account.balance.balance, str(account.id), str(account.id))
        )
        conn.commit()
        conn.close()




