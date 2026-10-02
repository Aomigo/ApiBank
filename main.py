import uuid

from fastapi import FastAPI, Depends, Body, HTTPException

from account import Account
from make_deposit import MakeDeposit
from make_transaction import MakeTransaction
from connect_user_JWT import generate_token, get_user
from in_memory_account_repository import Accounts
from in_memory_user_repository import Users
from inmemory_transaction_repository import InMemoryTransactionRepository
from check_pending import poll_pending
from cancel_transaction import cancel_transaction
import threading

app = FastAPI() 
    
Repo = Accounts()
repo_transaction = InMemoryTransactionRepository()

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

@app.get("/User/{id}/Info")
def get_user_info(id:str):
    allowed_info = {
        "name": Users.users[id].getUsername(),
        "email": Users.users[id].getEmail(),
    }
    return allowed_info


@app.post("/User/{id}/CreateAccount")
def create_Account(id:str):
    accId = str(uuid.uuid4())
    return Users.users[id].createAccount("Leugeu", accId, Repo, 0)

@app.get("/Useraccount/{id}/info")
def get_account_info(id:str):
    return Users.users[id].getAccount(id, Repo)
@app.get("/transaction/{id}")
def get_transaction(id: str):
    return repo_transaction.getById(id)


@app.post("/login")
def login(payload: dict = Body(...)):
    user_id = payload.get("id")

    if user_id not in Users.users:
        raise HTTPException(status_code=404, detail="User not found")
    storedUser = Users.users[user_id]
    return {"token": generate_token(storedUser)}

@app.get("/me", response_model=None)
def me(user=Depends(get_user)):
    return user
