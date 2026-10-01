from fastapi import FastAPI
from pydantic import BaseModel
from account import Account
from make_deposit import MakeDeposit
from make_transaction import MakeTransaction
from connect_user_JWT import TryConnectUser
from in_memory_account_repository import Accounts
from in_memory_user_repository import Users
from balance import Balance
from database import get_save_account
from user import User

app = FastAPI() 
    

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


#@app.get("/Balance")
#def get_balance():
    #return Balance(-1)

#A faire demain, faut JWT sur blackboard ( Ancien user connect)
#@app.post("User/connect")
#def connect_User():
    TryConnectUser()
    return
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




from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@app.post("/User/create/")
def create_user(user: UserCreate):
    new_user = User(id="", username=user.username, email=user.email, password=user.password)
    Users().save(new_user)
    return {"id": new_user.id, "name": new_user.username, "email": new_user.email}



