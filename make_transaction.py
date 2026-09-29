from repository_interface import AccountRepository

def MakeTransaction(amount, id1,id2,repository: AccountRepository):
    creditor = repository.getById(id1)
    receiver = repository.getById(id2)

    creditor.debiter(amount)
    receiver.crediter(amount)
    repository.save(receiver)
    repository.save(creditor)

    return
