from fastapi import FastAPI, HTTPException
from make_deposit import MakeDeposit
from make_transaction import MakeTransaction
from in_memory_account_repository import Accounts
from balance import Balance
from inmemory_transaction_repository import InMemoryTransactionRepository
from check_pending import poll_pending
from cancel_transaction import cancel_transaction
import threading

app = FastAPI() 
    
Repo = Accounts()
repo_transaction = InMemoryTransactionRepository()

#@app.post("/bank_account/open/{name}")
#def create_account(name: str):
#    account = account(name=name, solde=0, id=1)
#    return account


#@app.get("/Balance")
#def get_balance():
    #return Balance(-1)

@app.on_event("startup")
def startup():
    threading.Thread(target=poll_pending, args=(Repo, repo_transaction), daemon=True).start()


@app.post("/accounts/{id}/transactions")
def new_Transaction(id: str):
    return {"transaction_id": MakeTransaction(10, id, "2", Repo, repo_transaction)}


@app.post("/accounts/{id}/deposit")
def new_Deposit(id: str):
    MakeDeposit(10, id, Repo)
    return {"balance": Repo.getById(id).balance.balance}

@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    transaction = repo_transaction.getById(transaction_id)
    return {
        "id": transaction.id,
        "status": transaction.status,
        "amount": transaction.amount,
        "from": transaction.id_sender,
        "to": transaction.id_receiver,
    }

@app.get("/accounts/{id}")
def get_account(id: str):
    return {"id": id, "balance": Repo.getById(id).balance.balance}

@app.post("/transactions/{transaction_id}/cancel")
def cancel(transaction_id: str):
    transaction = repo_transaction.getById(transaction_id)
    try:
        cancel_transaction(transaction, Repo, repo_transaction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"id": transaction.id, "status": transaction.status}