class Curso:#Se crea una clase llamada Curso
    def __init__(self,titulo):#se crea una funcion con el constructor __init__ y se pone self para llamar los parametros de la clase
        self.__titulo=titulo#se pone self para actualizar la variable .__titutlo la cual esta enprivada y se le asigna el parametro titulo

    def getTitulo(self):#se crea un metodo y con getTitulo se llama el atributo 
        return self.__titulo#retorna y se actualiza el titulo en privado con self

class Aprendiz:#se crea una clase aparte llamada Aprendiz
    def __init__(self,nombre):#se crea un metodo y con el contructor(__init__)se inicializa el objeto de la clase
        self.__nombre=nombre#se llama el nombre privado con self y le asignamos nombre
        self.__cursos=[]#llamamos con el parametro self la variable cursos la cual es una lista

    def agregarCurso(self,nombreCursito):#se crea una metodo y le asiganamos una nueva variable,se llama los parametros con self
        cursito=Curso(nombreCursito)#creamos una nueva variable llamada cursito y llamamos la clase padre para asignarle el parametro (nombreCursito) 
        self.__cursos.append(cursito)#se llama con self a .__cursos y con append llamamos la variable cursito

    def getCursos(self):#creamos otro metodo y llamamos con get la variable cursos
        return self.__cursos #retorna lo que tenga la variable cursos
    
ap=Aprendiz('Sofia')#Se crea una variable llamada ap y le asignamos la clase Aprendiz,para asiganarle el nombre sofia
ap.agregarCurso('Python Basico')#con una variable ap.se llama el metodo agregarCurso y le asiganmos una cadena carecteres  
ap.agregarCurso('Python Intermedio')#Aca llamamos al metodo agregarCurso y le asignamos una cadena de caracteres

for c in ap.getCursos():#ponemos el bucle llamado for para que recorra con la variable c getCursos
    print(c.getTitulo())#llamos la varible c e imprimimos los atributos del metodo getTitulo
