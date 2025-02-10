
def elementos(lista1, lista2):
    resultado = [elemento for elemento in lista1 if elemento not in lista2]
    return resultado

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7]

resultado = elementos(lista1, lista2)
print("Elementos en la primera lista que no están en la segunda lista:", resultado)

