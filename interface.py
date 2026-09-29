from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def debiter(price, a):
        pass
    @abstractmethod
    def ajouter(price, a):
        pass
    


def make_transaction():
    pass