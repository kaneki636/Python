# Definimos el inicio (98), el fin (1004 para incluir el 1002) y el paso (2)
inicio = 98
fin = 1003

# Creamos el rango de números pares y los sumamos
suma_pares = sum(range(inicio, fin + 1, 2))

# Mostramos el resultado
print(f"La suma de los números pares entre 97 y 1003 es: {suma_pares}")