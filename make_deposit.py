from database import get_account_bdd , get_save_account

def MakeDeposit(amount, id1):
    receiver = get_account_bdd(id1)
    receiver.crediter(amount)
    get_save_account(receiver)

    return receiver.balance.balance




