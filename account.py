from balance import Balance


class Account:
    id:str
    def __init__(self, newname:str, newid:str , balance:int):
        self.name = newname,
        self.id = newid,
        self.balance= Balance(balance)
        self.opened

    def debiter(self, less:int ):
        self.balance= Balance(self.balance.balance - less)
        return
    def crediter(self, more:int ):
        self.balance= Balance(self.balance.balance + more)
        return
