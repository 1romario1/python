"""Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig.
manera:
Si trabaja 40 horas o menos se le paga $2600 por hora
Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40
horas y $5000 por cada hora extra"""
def pago(trabajo):
    pago_1 = trabajo * 2600
    pago_2 = (trabajo - 40)*5000
    if trabajo <= 40:
        print ("Su saldo sin extras es", pago_1 )
    else:
        print ("su saldo con extras es de ", pago_2 + 104000)

trabajo = int(input("cuantas horas elaboro?"))
pago(trabajo)