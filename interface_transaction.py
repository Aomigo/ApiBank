from transaction_body import Transaction
from abc import ABC, abstractmethod


class TransactionRepository(ABC):
    @abstractmethod
    def getById(self, id:str) -> Transaction:
        pass
    @abstractmethod
    def save(self, transaction:Transaction):
        pass