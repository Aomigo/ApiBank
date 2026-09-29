from abc import ABC, abstractmethod
from os import name


class Account:
    def __init__(self, newname:str, newid:str, newamount:int):
        self.name = newname,
        self.id = newid,
        self.amount = newamount

    def debiter(self, less:int):
        self.amount -= less
        return
    def crediter(self, amount):
        self.amount += amount
        pass


class AccountRepository(ABC):
    @abstractmethod
    def getById(self, id:str) -> Account:
        pass
    @abstractmethod
    def save(self, account:Account):
        pass

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

#requête post
def MakeTransaction(amount, id1,id2,repository: AccountRepository):
    creditor = repository.getById(id1)
    reciever = repository.getById(id2)

    creditor.debiter(amount)
    reciever.crediter(amount)

    return

accountInt = Accounts()
MakeTransaction(30, 1, 2, accountInt)