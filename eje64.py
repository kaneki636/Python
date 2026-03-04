
suma = 0
termino_actual = 1
contador_terminos = 0


while suma < 1.99:
    suma = suma + termino_actual
    

    contador_terminos = contador_terminos + 1
    
    print(f"Término {contador_terminos}: sumamos {termino_actual}, la suma va en {suma}")
    

    termino_actual = termino_actual / 2


print("¡Condición alcanzada!")
print("Número de términos necesarios:", contador_terminos)
print("Valor final de la suma:", suma)