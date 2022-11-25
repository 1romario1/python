'''Solicite una fecha al usuario. en formato día, mes y año. Dígale cuanto tiempo
ha pasado desde esa fecha hasta hoy o cuanto falta para llegar a esa fecha si es
posterior'''

import datetime
año=int(input("Ingrese un año: "))
mes=int(input("Ingrese un mes: "))
dia=int(input("Ingrese un dia: "))

fecha=datetime.datetime(año, mes, dia)
fecha_a=datetime.datetime.now()
diferencia =fecha -fecha_a
dias_p=diferencia.days

if dias_p -0:
    print("Han pasado ",dias_p, "dias")
else:
    print("Falta",dias_p)
    