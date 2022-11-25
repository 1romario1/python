#numeros primos
def primos (num):
    sum=sumaDivisor(num)
    if sum==1:
        return"Es primo"
    else:
        return"no es primo"
print(primos(12))
#esto se debe de pegar en ciclos
