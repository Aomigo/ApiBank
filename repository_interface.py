from abc import ABC, abstractmethod
from account import Account

class AccountRepository(ABC):
    @abstractmethod
    def getById(self, id:str) -> Account:
        pass
    @abstractmethod
    def save(self, account:Account):
        pass