#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. Sume los pares y saque el promedio de los impares
import random
from statistics import multimode
vec=[]
a=0
suma1=0
suma=0
cont=1
promedio=0
for i in range(random.randint(10,25)):
    vec.insert(i,round(random.random()*100))
    suma+=vec[i]
    a+=1
    if i%2==0:
        print("El numero es par",vec[i])
        suma1+=vec[i]
        cont=1
        promedio=suma1/cont
print("El promedio de los inpares es: ",promedio)
print(vec)