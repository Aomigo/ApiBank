from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from account import Account
from make_deposit import MakeDeposit
from make_transaction import MakeTransaction
from connect_user_JWT import TryConnectUser
from in_memory_account_repository import Accounts
from in_memory_user_repository import Users
from balance import Balance
from inmemory_transaction_repository import InMemoryTransactionRepository
from user import User
from check_pending import poll_pending
from cancel_transaction import cancel_transaction
import threading

app = FastAPI() 

Repo = Accounts()
repo_transaction = InMemoryTransactionRepository()
    

@app.post("/accounts/{id}/transactions")
def new_Transaction(id: str):
    result = MakeTransaction(10, "1", "2")
    return ("result : ", result)


@app.post("/accounts/{id}/deposit")
def new_Deposit(id: str):
    MakeDeposit(10, "1")
    return (" OK.")


#@app.post("/bank_account/open/{name}")
#def create_account(name: str):
#    account = account(name=name, solde=0, id=1)
#    return account

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


#@app.get("/Balance")
#def get_balance():
    #return Balance(-1)

#A faire demain, faut JWT sur blackboard

#@app.get("/User/{id}/Info")
#def get_user_info(id:str):
#    allowed_info = {
#        "name": Users.users[id].getUsername(),
#        "email": Users.users[id].getEmail(),
#    }
#    return allowed_info


@app.post("/User/connect")
def connect_User():
    return TryConnectUser()
@app.get("/User/{id}/Info")
def get_user_info(id: str):
    allowed_info = {
        "name": Users.users[id].getUsername(),
        "email": Users.users[id].getEmail(),
    }
    return allowed_info


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@app.post("/User/create/")
def create_user(user: UserCreate):
    new_user = User(id="", username=user.username, email=user.email, password=user.password)
    repo = Users()
    repo.save(new_user)
    account_id = repo.create_account(user_id=new_user.id, name=new_user.username)
    return {"id": new_user.id, "name": new_user.username, "email": new_user.email, "account_id": account_id,"balance": 0}

