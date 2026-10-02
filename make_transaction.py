import uuid
from transaction_body import Transaction


def MakeTransaction(amount, id1, id2, account_repo, transaction_repo):
    sender = account_repo.getById(id1)
    sender.debiter(amount)
    account_repo.save(sender)

    transaction = Transaction(id=str(uuid.uuid4()), id_sender=id1, id_receiver=id2, amount=amount)
    transaction_repo.save(transaction)
    return transaction.id
