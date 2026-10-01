from user import User
from user_repository_interface import UserRepository

class Users(UserRepository):
    users = {
        "1":User("1", "Bossu", "bossu@gmail.com", "mqlsdfkj"),
        "2":User("2", "Jane", "Jane@doe.com", "mqlsdfkj"),
        "3":User("3", "Dickinson", "Dicking@son.com", "mqlsdfkj")
    }
    def getById(self, id: str) -> User:
        return self.users[id]