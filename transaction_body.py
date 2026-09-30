from datetime import datetime


class Transaction:
    def __init__(self, id: str, id_sender: str, id_receiver: str , amount: int, status: str = "pending", emited_at: datetime = None):
        self.id = id
        self.id_sender = id_sender
        self.id_receiver = id_receiver
        self.amount = amount
        self.status = status
        self.emited_at = emited_at if emited_at is not None else datetime.now()