numero = (int(input('Escriba un numero: ')))

def variable(numero):
    print("Tabla del "+ str(numero))
    numero2=1
    while numero2 <=10:
        print(str(numero)+ "x" + str(numero2)+ " = "+ str(numero * numero2))
        numero2 +=1
    numero +=1

variable(numero)
