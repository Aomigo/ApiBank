from fastapi import FastAPI
from pydantic import BaseModel
from interface import Account

app = FastAPI()

    
#for get test
Kyky = Account(
    name="Kyky",
    id=5,
    solde=10
)

@app.post("/bank_account/create/{name}")
def create_account(name: str):
    account = Account(name=name, solde=0, id=1)
    return account

@app.get("/bank_account/{name}")
def return_account(name: str):
    #When saved, check name
    return Kyky

    
    