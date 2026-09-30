from command_input import cancel
pending = 1

async def transaction_pending():
    if pending == 5:
        cancel()
        return False
        print("transaction annulé")
    return True
