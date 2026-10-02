from repository_interface import AccountRepository



def MakeTransaction(amount: int, id1: str, id2: str, repository: AccountRepository, status:str = "pending"):
    creditor = repository.getById(id1)
    receiver = repository.getById(id2)

    creditor.debiter(amount)
    receiver.crediter(amount)

    repository.save(receiver)
    repository.save(creditor)

    return repository.getById(id1).balance.balance