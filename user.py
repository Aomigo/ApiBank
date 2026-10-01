from account import Account

class User:
    def __init__(self, id: str, username: str, email: str, password: str):
        if username == "" or password == "":
            raise AttributeError("Username & password are required.")
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.accounts = []

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email
