import random

cont1=1
suma=0

tam=round(random.randint(10,25))
vector=[round(random.random()*25) for i in range(25)]
print(vector)
for i in  range(len (vector)):
    suma += 1
    
print('suma',suma)

