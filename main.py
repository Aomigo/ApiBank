compte1Price = 0
compte2Price = 0

def virement(price, a, b):
    #fonction pour checker si négatif
    a -= price
    b += price
    return print(a, b)

virement(10, compte1Price, compte2Price)