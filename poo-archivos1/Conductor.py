class Conductor:#Creamos una clase llamada Conductor
    def __init__(self,nombre,documento):#Creamos un metodo __init__ y le agregamos dos parametros y cons elf indicamos que estamos dentro de la clase
        self.__nombre=nombre#creamos una variable para agregar el parametro nombre
        self.__documento=documento#Creamos una variable para agregar el parametro Documento
    def getNombre(self):#Creamos otro metodo llamado getNombre y le indicamos que estamos dentro
        return self.__nombre#retornamos el contenido de la variable __nombre
    def getDocumento(self):#Creamos otro metodo y llamamos los parametros de Documento e indicamos con self que estamos dentro de la clase
        return self.__documento#Retornamos el contenido de Documento
    