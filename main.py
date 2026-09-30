from fastapi import FastAPI
from make_deposit import MakeDeposit
from make_transaction import MakeTransaction
from in_memory_account_repository import Accounts
from balance import Balance
from inmemory_transaction_repository import InMemoryTransactionRepository

app = FastAPI() 
    
Repo = Accounts()
repo_transaction = InMemoryTransactionRepository()
@app.post("/accounts/{id}/transactions")
def new_Transaction(id:str):
    MakeTransaction(10,"1","2", Repo)
    print(Repo.accounts[id])

@app.post("/accounts/{id}/deposit")
def new_Deposit(id:str):
    MakeDeposit(10,"1", Repo)
    print(Repo.accounts[id].amount)


#@app.post("/bank_account/open/{name}")
#def create_account(name: str):
#    account = account(name=name, solde=0, id=1)
#    return account


#@app.get("/Balance")
#def get_balance():
    #return Balance(-1)

@app.get("/transaction/{id}")
def get_transaction(id: str):
    return repo_transaction.getById(id)
