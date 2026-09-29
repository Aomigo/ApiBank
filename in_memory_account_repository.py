from account import Account
from repository_interface import AccountRepository


class Accounts(AccountRepository):
    accounts = {
        "1":Account(newname="Kyky", newid="1", newamount=100),
        "2":Account(newname="Jojo", newid="2", newamount=60),
        "3":Account(newname="Thotho", newid="3", newamount=25)
    }

    def getById(self, id):
        return self.accounts[id]
    def save(self, account):
        self.accounts[account.id] = account
        return