"""Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
exceda los límites emita un mensaje y finalice el programa"""
def cifras(numero):
    if (numero<10):
        print("su numero es de una cifra")
    elif numero < 100:
        print ("el numero es de dos cifras")
    elif numero < 1000:
        print ("el numero es de tres cifras")
    elif numero < 10000:
        print ("el numero des de cuatro cifras")
    elif numero < 100000:
        print ("superastes el limite")
    
numero = int(input("digite su numero de 0 a 9999: "))
cifras(numero)