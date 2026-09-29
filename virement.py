from functions import Is_Sender_Negative
from fastapi import FastAPI
from pydantic import BaseModel
from bank_account import *

app = FastAPI()



@app.post("/virement/{price}")
def virement(price:int ,a: Account, b: Account):
    rawA = a.solde
    rawB = b.solde
    print(f"account {a.name} is sending money in account {b.name}")
    if Is_Sender_Negative(price, a.solde):
        print('error, account a too low, transaction cancelled')
        return
    a.debiter(price, a.solde)
    b.ajouter(price, b.solde)
    print(f"le compte a : {rawA} => {a.solde}, et le b : {rawB} => {b.solde}")
    return {a.name: a.solde, b.name: b.solde}
