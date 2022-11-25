x = int (input('digite el primer numero: '))
y = int (input('digite el segundo numero: '))
z = int (input('digite el tercer numero: '))

def num(x,y,z):

    if x == y == z :
        return("los tres numeros sojn inguales")
    elif x == y :
        return("el primero y segundo numeros son iguales")
    elif y == z :
        return("el segundo y tercer numeros son iguales")
    elif x == z :
        return("el tercer y primer numero son iguales")
    else :
        return("no hay numeros iguales")

print(num(x,y,z))
