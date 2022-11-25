#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios.
#Encuentre la moda de los números de la lista

import random
tamaño=round(random.randint(10,25))
vec=[]
vecCantidad=[]
for i in range(tamaño):
    vec.append(round(random.random()*100))
print(vec)
cont=0
for i in range(len(vec)):
    cont=0
    for j in vec:
        if vec[i]==j:
            cont+=1
    if cont!=0:
        vecCantidad.append(cont)
    else:
        vecCantidad.append(0)
print(vec)
print(vecCantidad)
mayor=0
pos=0
moda=0
for i in range (len(vec)):
    if mayor<vecCantidad[i]:
        mayor=vecCantidad[i]
print("El mayor es ",mayor)
for j in range(len(vecCantidad)):
    if mayor==vecCantidad[j]:
        moda=vecCantidad[j]
        print("la moda es:",vec[j])
        