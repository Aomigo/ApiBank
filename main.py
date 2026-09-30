from fastapi import FastAPI

from account import Account
from make_deposit import MakeDeposit
from make_transaction import MakeTransaction
from in_memory_account_repository import Accounts
from in_memory_user_repository import Users
from balance import Balance

app = FastAPI()
    
Repo = Accounts()
@app.post("/accounts/{id}/transactions")
def new_Transaction(id:str):
    MakeTransaction(10,"1","2", Repo)
    
  

@app.post("/accounts/{id}/deposit")
def new_Deposit(id:str):
    MakeDeposit(10,"1", Repo)



#@app.post("/bank_account/open/{name}")
#def create_account(name: str):
#    account = account(name=name, solde=0, id=1)
#    return account


@app.get("/Balance")
def get_balance():
    return Balance(-1)

@app.get("/User/{id}/Info")
def get_user_info(id:str):
    allowed_info = {
        "name": Users.users[id].username,
        "email": Users.users[id].email
    }
    return allowed_info
#create user test