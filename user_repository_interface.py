from abc import ABC, abstractmethod
from user import User
class UserRepository(ABC):
    @abstractmethod
    def getById(self, id: str) -> User:
        pass