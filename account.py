class Account:
    id:str
    def __init__(self, newname:str, newid:str, newamount:int):
        self.name = newname,
        self.id = newid,
        self.amount = newamount

    def debiter(self, less:int):
        self.amount -= less
        return
    def crediter(self, amount):
        self.amount += amount
        pass