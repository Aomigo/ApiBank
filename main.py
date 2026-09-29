from functions import Is_Sender_Negative
from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI() 

class Account(BaseModel):
    name: str
    id: int
    solde: int


Account1 = Account(name="compte1", id=1, solde=100)
Account2 = Account(name="compte2", id=2, solde=20)

@app.post("/virement/{price}")
def virement(price:int ,a: Account, b: Account):
    rawA = a.solde
    rawB = b.solde
    #price = Define_Price()
    #fonction pour checker si négatif
    print(f"account {a.name} is sending money in account {b.name}")
    if Is_Sender_Negative(price, a.solde):
        print('error, account a too low, transaction cancelled')
        return
    a.solde -= price
    b.solde += price
    print(f"le compte a : {rawA} => {a.solde} ,et le b : {rawB} => {b.solde}")
    return {a.name: a.solde, b.name: b.solde}