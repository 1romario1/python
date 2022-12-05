a=int(input("introduzca un numero: "))
b=int(input("Introduzca un numero: "))
c=int(input("Introduzca un numero: "))

def comparar(a,b,c):
    if(a==b):
        print("a y b son iguales")
        if (b==c):
            print("b y c son iguales")
        else:
            print("a es igual a b pero b es diferente a c")
    else:
        print("a y b son diferentes")

comparar(a,b,c)
