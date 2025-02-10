def encontrar_cadenas_vocales(lst):
    vocales = set("aeiouAEIOU")
    cadenas_con_vocales = [item for item in lst if isinstance(item, str) and sum(1 for char in item if char in vocales) >= 2]

    if cadenas_con_vocales:
        print("Cadena con dos o mas vocales:", ", ".join(cadenas_con_vocales))
    else:
        print("No existe")

lista = ["queso", "hambre", "pollo", "gris", "verde"]
encontrar_cadenas_vocales(lista)