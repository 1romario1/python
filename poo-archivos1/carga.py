from Vehiculo import *#decimos que de el modulo vehiculo importe todo
class Carga(Vehiculo):#creamos una clase llamada carga y l
    def __init__(self,placa,conductor,capacidad,ejes):#creamos metodos para nuestra clase e iniciamos con el contructor init los parametros
        Vehiculo.__init__(self,placa,conductor)#llamamos nuestro modulo e inicializamos los parametros
        self.__capacidad=capacidad#Indicamos que estamos en esta clase y a la variable capacidad le agregamos el parametro 
        self.__ejes=ejes#llamamos la variable ejes y le agregamos el parametro ejes    
    def getCapacidad(self):#creamos otro metodo llamado getcapacidad y le indicamos que estamos dentro con delf
        return self.__capacidad#retornamos el contenido del parametro    
    def getEjes(self):#creamos otro metodo llamado getEjes y le indicamos que estamos dentro
        return self.__ejes#retornamos el contenido del parametro