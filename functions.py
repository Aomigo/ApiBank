def Is_Sender_Negative(price, account):
    if account - price < 0:
        return True
    return False

def Suppr_Virement(price, a, b):
    b -= price
    a += price
    print ("Amount has been set back")
    return

def Define_Price():
    while True:
        choice = input("What is the desired amount? ")
        if choice.isdigit():
            return int(choice)
        print("Error, price isn't a digit. Please try again.")
#Function pour choisir destinataire