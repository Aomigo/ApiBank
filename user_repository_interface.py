from abc import ABC, abstractmethod
from create_account import User
class UserRepository(ABC):
    @abstractmethod
    def getById(self, id: str) -> User:
        pass