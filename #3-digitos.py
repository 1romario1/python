#numero de 3 digitos donde la suma del cubo de cada digito sea igaul al numero.
for n in range (100,1000):
    d=0
    suma=0
    i=n
    while 1 > 0:
        x=i%10
        z=i//10
        d=x**3
        suma += d
        i=z
    if suma==n:
        print("Estos numeros cumplen el requisito",n)