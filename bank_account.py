from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Account(BaseModel):
    name: str
    id: int
    solde: int
    


@app.post("/bank_account/create/{name}")
def create_account(name: str):
    account = Account(name=name, solde=0, id=1)
    return account

    
    