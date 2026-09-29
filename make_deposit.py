from repository_interface import AccountRepository

def MakeDeposit(amount, id1, repository: AccountRepository):
    receiver = repository.getById(id1)
    receiver.crediter(amount)
    repository.save(receiver)

    return




