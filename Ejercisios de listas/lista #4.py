#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
# Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)
import random
vec=[]
for i in range(random.randint(10,25)):
    vec.insert(i,round(random.random()*100))
new=True
while new:
    new = False
    for i in range (len(vec)- 1):
        if vec[i]> vec[i+1]:
            new =True
            vec[i], vec[i+1]= vec[i+1], vec[1]
print("Menor a mayor: ",vec)
new =True
while new:
    new =False
    for i in range(len(vec)- 1):
        if vec[i]<vec[i+1]:
            new =True
            vec[i], vec[i+1]= vec[i+1], vec[i]
print("Mayor a menor: ",vec)


