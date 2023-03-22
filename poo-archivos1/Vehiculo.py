class Vehiculo:#Creamos una clase llamada Vehiculo
    def __init__(self,placa,conductor):#Creamos otro metodo y le agregamos dos parametros e inicializamos con __init__
        self.__placa=placa#le agregamos la variable placa el parametro placa
        self.__conductor=conductor#le agregamos a la variable conductor el contenido del parametro conductor
    def getConductor(self):#creamos otro metodo y traemos el contenido de conductor
        return self.__conductor#Retornamos el contenido de la varibale conductor
    def getPlaca(self):#Creamos otro metodo y llamamos el contenido de la vaiable placa
        return self.__placa#retornamos el contenido de la variable placa