from balance import Balance
from datetime import datetime

class Account:
    id:str
    def __init__(self, newname:str, newid:str , balance:int, opened_at: datetime = None):
        self.name = newname
        self.id = newid
        self.balance= Balance(balance)
        self.opened_at = opened_at if opened_at is not None else datetime.now()

    def debiter(self, less:int ):
        self.balance= Balance(self.balance.balance - less)
        return
    def crediter(self, more:int ):
        self.balance= Balance(self.balance.balance + more)
        return
