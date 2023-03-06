class A1:#Se crea una clase llamada A1
    def __init__(self):#Se crea un metodo y se inicia con el contrcutor __init__
        pass#ponemos una pass para indicar que hay un 
    def saludo(self):#creamos un metodo llamado saludo
        print('Hola desde A1')#imprimimos un string 

class A2:#Se crea una clase aparte llamada A2
    def __init__(self):#creamos un metodo para esta clase
        pass#para que no este vacio ponemos pass
    def saludo(self):#creamos otro metodo llamado saludo
        print('Hola desde A2')#imprimimos 


class B(A2,A1):#creamos otra clase aparte llamda B y llamamos la clase A1 y A2
    def __init__(self):#iniciamos con el constructor __init__ la instancia de mi clase
        pass#ponemos pass
    def saludo(self):#creamos otro metodo llamado saludo
        print('Hola desde B')#imprimimos esta cadena de texto
    def __str__(self):#creamos otro metodo para iniciar el metodo str
        return 'Soy un objeto de la clase B'#retornamos la cadena string 
obj=B()#creamos un objeto para asignar B
print(obj.__str__())#imprimimos el objeto str y en pantalla saldra soy un objeto de la clase B
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())