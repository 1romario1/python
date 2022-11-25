import random
vec={}
tam=round(random.randint(5,10))

vec2=[0 for i in range(tam)]
print(vec2)

vec3=[(i+1)**0.5 for i in range(tam)]
print(vec3)

import random


vector=[round(random.random()*100) for i in range(10)]
print(vector)


pares=[x for x in vector if x%2==0]
impares=[x for x in vector if x%2!=0]

print(pares)
print(impares)

pares2=[x if x%2==0 else 0 for x in vector]
print(pares2)

undigito=(x if x<10 else 0 for x in vector)

print(undigito)

edad=['maryor' if x>=18 else 'menor' for x in vector]
print(edad)





