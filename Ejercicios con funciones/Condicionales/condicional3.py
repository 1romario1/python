"""Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores"""
def calificacion(nota):
    if nota<=2:
        print("su calificacion es insuficiente ")
    elif nota<=4:
        print("su calificacion es suficiente ")
    elif nota<=6:
        print("sacaste buena calificacion ")
    elif nota<=8:
        print("su calificacion es superior ")
    elif nota<=10:
        print("su calificacion es exelente ")
nota = int(input("su calificacion es: "))
calificacion(nota)