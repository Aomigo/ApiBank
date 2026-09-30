class Transaction:
    def __init__(self, id: str, id_sender: str, id_receiver: str , amount: int, status: str = "pending"):
        self.id = id
        self.id_sender = id_sender
        self.id_receiver = id_receiver
        self.amount = amount
        self.status = status
        self.emited_at = None