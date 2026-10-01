from transaction_body import Transaction
from abc import ABC, abstractmethod
from interface_transaction import TransactionRepository



class InMemoryTransactionRepository(TransactionRepository):
    transactions = {
        
    }

    def getById(self, id: str) -> Transaction:
        return self.transactions[id]

    def save(self, transaction: Transaction):
        self.transactions[transaction.id] = transaction
        return

    def get_pending_transactions(self):
        return [
            transaction
            for transaction in self.transactions.values()
            if transaction.status == "pending"
        ]