n = int(input("Ingrese un numero: "))
suma = 0
for i in range(1,n):
    if n % i == 0:
        suma += i
if suma == n:
    print("El numero SI es perfecto")
else: print("El numero NO es perfecto")