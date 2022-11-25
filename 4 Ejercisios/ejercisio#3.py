#numeros de 3 digitos donde la suma del cubo de cada digito sea igual al numero.
for m in range(100,1000):
    md=0
    suma=0
    i=m
    while i > 0:
        x=1%10
        n=i//10
        md=x**3
        suma+=md
        i=n
    if suma==m:
        print(m)