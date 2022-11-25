import random
def llenarLista(list):
    tam=round(random.randint(2,20))
    for i in range(tam):
        list.append(round(random.randrange(100)))
    return list

def sumarLista(list):
    sum=0
    for i in range(20):
        sum+=i
    return sum

lista=[]
lista=llenarLista(lista)
print(lista)
print("la suma es=",sumarLista(lista))


