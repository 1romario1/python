#2. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con 
# números aleatorios. Muestre cuales y cuantos son primos
import random
cont1=0
cont2=0
suma1=0
tamaño=random.randint(10, 25)
vec=[]
for i in range (tamaño):
    vec.insert(1,round(random.randint(0, 100)))
print(vec)

for i in range(len(vec)):
    if vec [i]% 2==0:
        cont1=cont1+1
    if cont1 > 2:
        continue
    else:
        print(vec[i], " el numero es primo")
        cont2=cont2+1
        suma1=suma1+vec[i]
print("la cantidad de numero primos es: ",cont2)
print("la suma de los numeros primos es igual a: ",suma1)