from transaction_body import Transaction
from abc import ABC, abstractmethod
from interface_transaction import TransactionRepository
from database import get_db_connection

STATUS_MAP = {"pending": "1", "canceled": "2", "completed": "3"}


class InMemoryTransactionRepository(TransactionRepository):
    transactions = {}

    def getById(self, id: str) -> Transaction:
        return self.transactions.get(id)

    def save(self, transaction: Transaction):
        self.transactions[transaction.id] = transaction
        conn = get_db_connection()
        statut = STATUS_MAP.get(transaction.status, "1")

        # Si la transaction a déjà un id en BDD, on met à jour le statut (passage à 3 = accepted ou 2 = annulé)
        if hasattr(transaction, "db_id") and transaction.db_id:
            conn.execute(
                'UPDATE "transaction" SET statut = ? WHERE id = ?',
                (statut, transaction.db_id)
            )
        else:
            cursor = conn.execute(
                'INSERT INTO "transaction" (id_sender, id_receiver, amount, statut) VALUES (?, ?, ?, ?)',
                (transaction.id_sender, transaction.id_receiver, transaction.amount, statut)
            )
            transaction.db_id = cursor.lastrowid

        conn.commit()
        conn.close()

    def get_pending_transactions(self):
        return [
            transaction
            for transaction in self.transactions.values()
            if transaction.status == "pending"
        ]

    