spotify={}
def ARTISTA(spotify):
    ARTISTA=input("ingrese el artista: ")
    spotify.update({ARTISTA:{}}) 
    return spotify
def informacionartista(spotify):
    ARTISTA=input("ingrese el artista: ")
    if ARTISTA not in spotify:
        print('El artista no se encuentra, agreguelo primero')
        return spotify
    cancion=input("Ingrese el nombre del cancion: ")
    genero=input("Ingrese el genero musical: ")
    duracion=input("Ingrese la duracion en formato xx(mm):xx(ss): ")
    if ARTISTA in spotify:
        spotify.update({ARTISTA:{"cancion":cancion,"genero":genero,"duracion":duracion}})
        
def buscarcancion(spotify):
    buscar=input("que cancion quiere buscar:  ")
    for i in sorted(spotify.values()):
        if buscar==i['cancion']:
            print("la cancion",buscar, "se encuentra en spotify y su duracion es:",i["duracion"])
            return None
    print("la cancion no se encuentra, ingrese el nombre primero")
    
def buscarartista(spotify):
    buscar=input("que artista desea buscar: ")
    for x in (spotify.keys()):
        if buscar==x:
            print("el artista",buscar, "se encuentra en spotify y su genero es:",spotify[x]["genero"])
            return None
    print("el artista no se encuentra, ingrese la cancion con el artista")