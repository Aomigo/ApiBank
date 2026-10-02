from datetime import datetime


class Transaction:
    def __init__(self, id, id_sender, id_receiver, amount, status="pending", emited_at=None):
        self.id = id
        self.id_sender = id_sender
        self.id_receiver = id_receiver
        self.amount = amount
        self.status = status
        self.emited_at = emited_at if emited_at is not None else datetime.now()

    def change_to_canceled(self):
        self.status = "canceled"

    def change_to_completed(self):
        self.status = "completed"