"""Calcular todos los números de 3 cifras tales que la suma
de los cubos de las cifras es igual al valor del número."""

int(input("ingrese el numero de 3 cifras: "))
n=0
a=0
a=int(n/100)
b=int(n/10)- (a*10)
c=n-(a*100+b*10)
resultado=str(a^2+b^2+c^2)
while resultado ==1000:
    print("la suma de los cuadrados del numero",n,"es igual a : ",resultado)
else:
    print("error digite un numero de 3 cifras")
    print("ingrese un numero de 3 cifras: ")
print("la suma de los cuadrados del numero ",n," es igual a : ",resultado)
print("fin del programa")


