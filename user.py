from account import Account


class User:
    def __init__(self,id:str, username,email, password):
        if username == "" or password == "":
            raise AttributeError("Username & password are required.")
        self.id = id
        self.username = username
        self.email = email
        self.password = hash(password)
        self.accounts = []

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def createAccount(self,name,id,balance:int = 0):
        self.accounts.append(Account(name,id,balance))
        return self.accounts