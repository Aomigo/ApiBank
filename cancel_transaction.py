from datetime import datetime, timedelta


def cancel_transaction(transaction, account_repo, transaction_repo):
    if transaction.status != "pending":
        raise ValueError("Transaction is not pending")
    if transaction.emited_at <= datetime.now() - timedelta(seconds=30):
        raise ValueError("Too late to cancel (more than 30s)")

    sender = account_repo.getById(transaction.id_sender)
    sender.crediter(transaction.amount)
    account_repo.save(sender)

    transaction.change_to_canceled()
    transaction_repo.save(transaction)