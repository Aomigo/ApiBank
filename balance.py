

class Balance:
    def __init__(self, balance: int ):
        if balance < 0:
            raise ValueError("Operation canceled your balance cannot be negative")
        self.balance = balance

    def add_money(self, amount: int):
        return Balance(self.balance + amount)

    def remove_money(self, amount: int):
        return Balance(self.balance - amount)
