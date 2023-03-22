from Conductor import *#Indicamos que del modulo Conductor importeme todo
from carga import *#Indicamos que del modulo cargar importeme todo
lista=[]#creamos una lista vacia
with open('poo-archivos/listado.txt','r') as flujo:#indicamos que habra la direccion
    for ob in flujo:#ponemos un for que recorrar flujo
        lista.append(ob)#y le agregamos a la lista la variable ob la cual tiene el contenido de flujo
i=0#creamos un contador
for ob in lista:#recorremos ob en lista
    lista[i]=ob.rstrip()#decimos que lista ya no esta vacia si no tiene el contenido de i,yu ponemos un rstrip para eliminar los espacios en blanco al final de la cadena
    i+=1#le indicamos que cuando no se cumpla le sume uno al contador
print(lista)#imprimimos la lista
#placa, nombre,doc, cap, ejes
lautos=[]#creamos otra lista vacia
for ob in lista:#recorremos lista con ob
    #for x in ob.split(','):
    lautos.append(ob.split(','))#a la lista lautos le agregamos el objeto ob,y ponemos .split para convertir una cadena en una lista
cargas=[]#Creamos una nueva lista
print(lautos)#imprimimos la lista lautos
for i in range(len(lautos)):#pedimos con un for que i recorra en un rango de todos los indices de la lista lautos
    #print(lautos[i][0])    
    p=lautos[i][0]#creamos varias variables y le agreamos a la lista lo que recorrio i
    n=lautos[i][1]
    d=lautos[i][2]
    c=lautos[i][3]
    e=lautos[i][4]
    con=Conductor(n,d)#creamos otra variable y le agregamos conductor para llamar las varibles n y d
    obj=Carga(p,con,c,e)#creamos un objeto y le agregamos carga con las variables restantes
    cargas.append(obj)#llamamos a cargas y le agregamos el objeto obj

print(cargas)#imprimimos cargas 
# 
# for ob in lautos:
    
#     #for x in ob:
#      #   print(x)
#         # p=x[0]
#         # n=x[1]
#         # d=x[2]
#         # c=x[3]
#         # e=x[4]
#         # con=Conductor(n,d)
#         # obj=Carga(p,con,c,e)
#         # cargas.append(obj)
# print(cargas)