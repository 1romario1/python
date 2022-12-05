cont=0
cont2=0
sumaimpar=1
sumapar=1

import random
tam=int(input('Ingrese cantidad'))
vec=[]
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
for i in range(len(vec)):
    if vec [i]%2 == 0:
        print(vec[1],'par')
    else:
        print(vec[1],' impar')
        cont+=1 
print("finaliza")

print ( "cuantos pares", cont)
print("cuantos impares", cont)

sumaimpar=+ vec[i]
print("suma de los pares",sumaimpar)
sumapar=+ vec[i]
print("suma de los pares", sumapar)





        
    
