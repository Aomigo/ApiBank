from account import Account

class Balance(Account):
    def __init__(self, balance: int ):
        #self.account = Account(id)
        if balance < 0:
            raise ValueError("Operation canceled your balance cannot be negative")
        self.balance = balance

