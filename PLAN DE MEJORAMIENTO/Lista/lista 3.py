
def elevar_2(numero : int, lista: list):
    for i in range (0, len(lista)):
        lista[i]= lista[i]**2
    numero=numero**2
    input()
def main():
    numero=10
    lista=[1, 2, 3, 4, 5]
    print("la lista original es", lista, "y el numero es", numero)
    elevar_2(numero, lista)
    print("Tras aplicar la funcion de elevar al cuadradp ambos elementos:")
    print("la lista es", lista, "y el numero es" , numero)

main()

    