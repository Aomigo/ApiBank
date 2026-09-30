class User:
    def __init__(self,id, username,email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = hash(password)

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

