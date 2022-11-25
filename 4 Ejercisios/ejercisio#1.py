#pedir numero,imprimirlo con el opuesto
#(ejemplo 5 opuesto -5,-10 opuesto 10).finaliza con cero y diga cuantos ingreso

i=1
cont=0

while i != 0:
    i=int(input("Escriba un numero: "))
    if i !=0:
        print(i,"opuesto", -(i))
        cont+=1
    if i ==0:
        print("finalizacion del programa")
print("ingresado",cont,"numero")

