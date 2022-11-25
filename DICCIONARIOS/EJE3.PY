#PRUEBA ATLETICA

PRUEBA_ATLETICA = {}

while True:
    nombre = input("Ingresar el nombre de la atleta: ")
    if nombre == "":
        break

    distancia= int(input("Ingresa la distancia de salto (0-8mt): "))
    if distancia not in range(1,8):
        break
    
    if nombre in  PRUEBA_ATLETICA:
        PRUEBA_ATLETICA[nombre] += (distancia,)
    else:
        PRUEBA_ATLETICA[nombre] = (distancia,)
        
for nombre in sorted(PRUEBA_ATLETICA.keys()):
    adding = 0
    counter = 0
    for distancia in PRUEBA_ATLETICA[nombre]:
        adding += distancia
        counter += 1
    print(nombre, ":", adding / counter)
    
print()


"MIRAR EN REPOSITORIO PARA TERMINAR"
    
