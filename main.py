from functions import Is_Sender_Negative

compte1Price = 10
compte2Price = 20



def virement(price, a, b):
    #fonction pour checker si négatif
    if(Is_Sender_Negative(price, a)):
        return print('error, account a too low, transaction cancelled')
    a -= price
    b += price
    return print(a, b)

virement(10, compte1Price, compte2Price)