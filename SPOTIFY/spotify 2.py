lista1 ={}
def agregar(list,artista):
    list[artista]={}
    return list


f={}
print(agregar(f,"i"))

def agregar_l(list,artista,cancion,genero,duracion):
    if artista in list:
        list[artista][cancion]={}
    agregar=(input("agregar artista"))
    return list



