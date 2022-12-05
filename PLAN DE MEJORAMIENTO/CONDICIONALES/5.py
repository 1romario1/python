#Solicite un numero al usuario e imprima todos los pares que esten antes de ese numero.

n = int(input('Escriba un numero: '))

def par(n):
    for item in range(2, n+1, 2):
        print(item, end=",")
    else:
        print("fin.")

par(n)