'''Solicite un Angulo al usuario en grados. Diga en que cuadrante está. Diga
además en que vuelta está sabiendo que cada 360 grados se completa una
vuelta a la circunferencia. Además diga el resultado en radianes.'''

from math import pi, trunc

angulo1 = int(input("Ingrese el ángulo en grados:  "))
angulo=angulo1
if angulo<0:
    print ("No digitastes ningún ángulo")
else:
    vuelta = trunc(angulo/360)
    angulo = angulo - (vuelta*360)
    radianes = angulo1*pi/180
    if angulo >0 and angulo<=90:
        print("Está en el cuadrante #: 1 y esta en la vuelta # ",vuelta+1," a la circunferencia y en radianes es: ",radianes)
    elif angulo >90 and angulo<=180:
        print("Está en el cuadrante #: 2 y esta en la vuelta # ",vuelta+1," a la circunferencia y en radianes es: ",radianes)
    elif angulo>180 and angulo<=270:
        print("Está en el cuadrante #: 3 y esta en la vuelta # ",vuelta+1," a la circunferencia y en radianes es: ",radianes)
    else:
        if angulo==0:
            print("Está en el cuadrante #: 4 y esta en la vuelta # ",vuelta," a la circunferencia y en radianes es: ",radianes)
        else:
            print("Está en el cuadrante #: 4 y esta en la vuelta # ",vuelta+1," a la circunferencia y en radianes es: ",radianes)