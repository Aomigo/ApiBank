from database import get_account_bdd, get_save_account 



def MakeTransaction(amount: int, id1: str, id2: str, ):
    creditor = get_account_bdd(id1)
    receiver = get_account_bdd(id2)


    creditor.debiter(amount)
    receiver.crediter(amount)
    get_save_account(receiver)
    get_save_account(creditor)

    return creditor.balance.balance
    