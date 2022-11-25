import random
from statistics import mode
vec=[]
a=0
suma=0
cont=0

for a in range(random.randint(10,25)):
    vec.insert(0,round(random.random()*100))
    suma += vec[a]
    cont+= 1
    suma==suma/cont
    promedio=suma/cont
    if a < promedio:
        print(a,"El numero esta por debajo del promedio")
    elif a > promedio:
        print(a,"El numero esta por encima del promedio")
    else:
        print(a,"El numero es igual al promedio")




	