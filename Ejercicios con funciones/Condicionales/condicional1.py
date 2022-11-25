#pedir 3 numero e indicar cual es el medio
def mayor(x=int(input('digite el primer numero: ')),
          y=int(input('digite el segundo numero: ')),
          z=int(input('digite el tercer numero: '))):
    if x>y and x<z:
        print("El numero",x,"es el numero del medio")
    elif x>z and x<y:
        print("El numero",x,"es el numero del medio")
    elif y>x and y<z:
        print("El numero",y,"es el numero del medio")
    elif y<x and y>z:
        print("El numero",y,"es el numero del medio")
    elif z<x and z>y:
        print("El numero",z,"es el numero del medio")
    elif z>x and z<y:
        print("El numero",z,"es el numero del medio")
    elif x==y:
        print("No se puede calcular el valor del medio")
    elif x==z:
        print("No se puede calcular el valor del medio")
    elif x==z:
        print("No se puede calcular el valor del medio")
    else:
        print("Todos son iguales")

mayor()