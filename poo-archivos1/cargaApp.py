from carga import *#Indicamos que del modulo cargar importe todo
from Conductor import *#Indicamos que del modulo conductor importe todo
# c1=Conductor('Luis',12345)
# carga1=Carga('aaa-123',c1,5,2)
# print(carga1)
nomConductor=input('Ingrese nombre del conductor')#le pedimos un nombre al usuario
docConductor=int(input('Ingrese documento del conductor'))#le pedimos un numero de documento al usuario
placa=input('ingrese placa')#le pedimos al usuario que ingrese la placa
capacidad=input('ingrese capacidad en toneladas')#le inicidamos al usuario que digite una cantidad de toneladas
ejes=input('ingrese numero de ejes')#Le indicamos al usuario que ingrese una cantidad de ejes
c1=Conductor(nomConductor,docConductor)#llamamos al modulo conductor y le agregamos la variable nomConductor y docConductor
obCarga=Carga(placa,c1,capacidad,ejes)#llamamos al modulo cargar y le agregamos las variables restantes las cuales tienen informacion del usuario
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento())#A la variable conductor le agregamos un objeto para la carga y con get llamamos los atributos y los conactenamos con una cadena de texto y adentro los mismos valores


cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes())#

with open('poo-archivos/listado.txt','a') as flujo:#indicamos que con open habra la sigiente direccion y con as le indicamos que la habra como flujo
    flujo.write(cadCarga+'\n')#y aca ponemos en flujo el metodo write que indica para escribir y con \n le damos un salto de linea