from repository_interface import AccountRepository


def MakeDeposit(amount: int, id1: str, repository: AccountRepository):
    receiver = repository.getById(id1)
    receiver.crediter(amount)
    repository.save(receiver)
    return receiver.balance.balance