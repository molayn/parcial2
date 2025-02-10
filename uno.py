def lista_sin_repetidos(lst):
    if len(lst) == len(set(lst)):
        print("no hay elementos repetidos")
    else:
        print("si hay elementos repetidos")

lista = [1, 2, 3, 2, 5]

print(f"Lista {lista}: ", end="")
lista_sin_repetidos(lista)