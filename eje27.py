#cientifico 

valor1 = float(input("Ingrese el primer valor de la figura:"))
valor2 = float(input("Ingrese el segundo valor de esta figura:"))
valor3 = float(input("Ingrese el tercer valor de esta figura:"))

posible_triangulo = (valor1 * valor2) /2
posible_rectangulo = valor1 * valor2
posible_circulo = valor2* ( valor1 ** 2)


if posible_triangulo ==valor3:
    print(f"Haz concidido con el area del trianfulo {posible_triangulo}")
    
elif posible_rectangulo == valor3:
    print(f"Haz concidido con el area del rectangulo {posible_rectangulo}")
    
elif posible_circulo ==valor3:
   print(f"Haz concidido con el area del circulo {posible_circulo}")

elif valor3 not in [posible_triangulo, posible_rectangulo, posible_circulo]:
    print("No hay coincidencia con ninguna figura conocida.")
    