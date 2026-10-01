def complete_transaction(transaction, account_repo, transaction_repo):
    receiver = account_repo.getById(transaction.id_receiver)
    receiver.crediter(transaction.amount)
    account_repo.save(receiver)

    transaction.change_to_completed()
    transaction_repo.save(transaction)