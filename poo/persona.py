class Persona:#crea  un clase llamada persona
    def __init__(self,nombre):#se crea una funcion y un constructor(__init__)el cual sirve para crear un objeto(instancia),y se utiliza la palabra clave self para inicializar los atributos que pertenezcan a esta clase
        self.__nombre=nombre#aqui se llama la variable nombre con self,es un atributo
        print('Activando constructor')#y se ejecuta esta instruccion

    def getNombre(self):#se crea otra variable
        return self.__nombre#retorna 
    
    def setNombre(self, nombre):#se crea una nueva variable y se pone el argumento nombre
        self.__nombre=nombre#se llama con self y se asigna al argumento nombre

    def metodo(self):
        print('Soy un método')


ob=Persona('Ana')#se crea una varibale y se asigna la clase persona
print(ob.getNombre())#se ejecuta esta instruccion
ob.setNombre('Maria')
print(ob.getNombre())
#ob.metodo()
#print(type(ob))