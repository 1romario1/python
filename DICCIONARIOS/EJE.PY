d={}
dict={
    "gato":"cat",
    'perro': 'dog',
    'vaca':'cow',
    'caballo':'hourse',
}   
#sorted()
print(dict)
print(dict.get('perro'))
print(dict['vaca'])

#metodo del
del dict["perro"]
print(dict)

#metodo update
dict.update({"perro":"dog"})
print(dict)

#metodo popitem
dict.popitem()
print(dict)

#metodo keys
for i in dict.keys():
    print(i)

#metodo value
for i in dict.values():
    print(i)
    
for k,v in dict.items():
    print(k,'´->',v)

for item in dict.items():
    print(item)
    
