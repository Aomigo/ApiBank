from account import Account
from repository_interface import AccountRepository

class Accounts(AccountRepository):
    accounts = {
        "1":Account(newname="Kyky", newid="1", balance=100),
        "2":Account(newname="Jojo", newid="2", balance=60),
        "3":Account(newname="Thotho", newid="3", balance=25)
    }

    def getById(self, id:str) -> Account:
        return self.accounts[id]
    def save(self, account:Account):
        Accounts.accounts[account.id] = account
        return