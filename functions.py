def Is_Sender_Negative(price, account):
    if account - price < 0:
        return True
    return False
