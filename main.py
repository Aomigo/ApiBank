from functions import Is_Sender_Negative

compte1Price = 10
compte2Price = 20



def virement(price, a, b):
    rawA = a
    rawB = b
    #fonction pour checker si négatif
    if(Is_Sender_Negative(price, a)):
        print('error, account a too low, transaction cancelled')
        return
    a -= price
    b += price
    print(a,b)
    print(f"le compte a : {rawA} => {a} ,et le b : {rawB} => {b}")
    return


virement(10, compte1Price, compte2Price)