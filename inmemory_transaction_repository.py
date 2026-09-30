from transaction_body import Transaction
from abc import ABC, abstractmethod
from interface_transaction import TransactionRepository



class InMemoryTransactionRepository(TransactionRepository):
    transactions = {
        "1": Transaction(id="1", id_sender="1", id_receiver="2", amount=100, status="completed"),
        "2": Transaction(id="2", id_sender="2", id_receiver="3", amount=60),
        "3": Transaction(id="3", id_sender="3", id_receiver="1", amount=25)
    }

    def getById(self, id: str) -> Transaction:
        return self.transactions[id]

    def save(self, transaction: Transaction):
        self.transactions[transaction.id] = transaction
        return
