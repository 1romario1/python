class Aprendiz:#creamos una clase llamada Aprendiz
    def __init__(self,nombre):#Iniciamos con nuestro constructor __init__ los parametros de nuestra clase
        self.__nombre=nombre#llamamos nuestro parametro con self  y ponemos en privado el nombre
        self.__cursos=[]#creamos una nueva variable que tiene un contenido de lista vacia

    def agregarCurso(self,titulo):#creamos un metodo llamado agregarCurso y le asignamos dos parametros
        self.__cursos.append(titulo)#llamamos y agregamos a nuestra variable cursos el parametro titulo

    def getCursos(self):#creamos otro metodo que se llama getCursos y le ponemos nuestro parametro self
        return self.__cursos#retorna la variable cursos

class Curso:#se crea una clase llamada Curso
    def __init__(self,titulo):#Se inicializa la intancia de esta clase con el contructor __init__
        self.__titulo=titulo#Se llama el parametro titulo

    def getTitulo(self):#Se crea otro metodo y se devuelve el valor con get
        return self.__titulo#retorna el parametro titulo 
    
a=Aprendiz('Martha')#Se crea una variable para almacenar Aprendiz y de nombre darle 'Marta'
c1=Curso('Python Intermedio')#Se crea una nueva variable y se llama la clase curso 
c2=Curso('Python Basico')#Se crea una nueva variable y se llama la clase curso para agregarle la cadena de texto Python Basico
c3=Curso('Introduccion a Java')#Se crea una nueva variable y se le asigna la clase curso y nuevamente se le agrega una cadena string

a.agregarCurso(c1)#Se crea un objeto y se llama el metodo agregarCurso para asignarle la variable c1
a.agregarCurso(c2)#Se crea un objeto y se llama el metodo agregarCurso para asignarle la variable c2
a.agregarCurso(c3)#Se crea un objeto y se llama el metodo agregarCurso para asignarle la variable c3

print(a.getCursos())#imprimimos nuestra variable