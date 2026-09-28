from functions import Is_Sender_Negative
from functions import Suppr_Virement
from functions import Define_Price
compte1Price = 10
compte2Price = 20



def virement(a, b):
    rawA = a
    rawB = b
    price = Define_Price()
    #fonction pour checker si négatif
    if Is_Sender_Negative(price, a):
        print('error, account a too low, transaction cancelled')
        return
    a -= price
    b += price
    print(a,b)
    print(f"le compte a : {rawA} => {a} ,et le b : {rawB} => {b}")
    choice = input("Amount sent, cancel (y/N)?")
    if choice == "y":
        Suppr_Virement(price, a, b)
    return


virement(compte1Price, compte2Price)