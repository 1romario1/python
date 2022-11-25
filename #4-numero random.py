import random

x= random.randint(1,10)
n=0
cont=0

while n !=x:
         n = int(input("Escriba un numero"))
         cont += 1
         if n > x:
                print(n,"Es muy grande")
else:
            print(n,"Es muy pequeño") 
print("Numero de intentos = ",cont)            