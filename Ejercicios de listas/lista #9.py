#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la 
#lista con números aleatorios. Encuentre la mediana de los números de la lista

import random
tam,prom,suma=0,0,0
vec=[int(random.random()*100)for i in range(10,25)]
print(vec)
for i in range(len(vec)):
    for y in range(i+1,len(vec)):
         if vec[i]> vec[y]:
            vec[i], vec[y] = vec[y], vec[i]
print("Arreglo de menor a mayor:\n", vec)
if tam%2>0:
    mediana=vec[vec[tam//2]]
else:
    mediana=(vec[tam//2]+vec[tam//2-1])/2
print("la mediana es: ",mediana)