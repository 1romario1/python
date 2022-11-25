#Ternas pitagoricas. Un tringulo rectangulo puede tener lados que sean todos enteros, el conjunto de 3 valores enteros para los lados de un triangulo rectangulo se conoce como una terna pitagorica. Estos 3 lados deben satisfacer la relacion que la suma de los cuadrados de los dos lados es igual al cuadrado de la hipotenusa.
#Encuentre todas las ternas pitagóricas para el lado 1, lado 2 y la hipotenusa,
#todos ellos no mayores que 500. ejemplo c=3,c=4,h=5

for s in range(1, 501):
    for l in range (1,501):
        x= s**2 + l**2
        for i in range (1,501):
            m= i**2
            if x==m:
                print("ca", s, ",co=", l, ".h=", )