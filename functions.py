def Is_Sender_Negative(price, account):
    if account - price < 0:
        return True
    return False

def Suppr_Virement(price, a, b):
    b -= price
    a += price
    print ("Amount has been set back")
    return