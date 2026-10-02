from pydantic import BaseModel

from account import Account
from repository_interface import AccountRepository


class User:
    def __init__(self,id:str, username:str,email:str, password:str):
        if username == "" or password == "":
            raise AttributeError("Username & password are required.")
        self.id = id
        self.username = username
        self.email = email
        self.password = hash(password)
        self.accountting = ["2"]

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def createAccount(self,name:str,accId:str, repository: AccountRepository, balance:int = 0):
        newAccount = Account(name,accId,balance)
        self.accountting.append(accId)
        repository.save(newAccount)
        return self.accountting

    def getAccount(self, accountId, repository: AccountRepository):
        return repository.getById(accountId)