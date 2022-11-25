def sumaDivisor(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma


#¿numeros son perfectos o inperfectos?


def perfectos(num):
    sum=sumaDivisor(num)
    if sum==num:
        return 'perfecto'
    else:
        return 'no es perfecto'

print(perfectos(25))

def primos (num):
    sum=sumaDivisor(num)
    if sum==1:
        return"Es primo"
    else:
        return"no es primo"
print(primos(12))
