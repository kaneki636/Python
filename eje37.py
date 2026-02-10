longitud1 = int(input("Ingrese un numero (entero positivo):"))
longitud2 = int(input("Ingrese un numero (entero positivo):"))
longitud3 = int(input("Ingrese un numero (entero positivo):"))

#validar si es un triangulo
lado_mayor= max(longitud1, longitud2, longitud3)
suma_menores = longitud1 + longitud2 + longitud3 - lado_mayor

#posiblles concidencias
if suma_menores > lado_mayor:
    print("Si es un triangulo") 

    if longitud1 == longitud2 == longitud3:
        print("Es un triangulo equilatero")

    elif longitud1 == longitud2 or longitud1 == longitud3 or longitud2 == longitud3:
        print("Es un triangulo isosceles")

    else:
        print("Es un triangulo escaleno")

    #area del triangulo
    s = (longitud1 + longitud2 + longitud3) / 2
    area = math.sqrt(s * (s - longitud1) * (s - longitud2) * (s - longitud3))
    print("El área del triángulo es:", round(area, 2))

else: 
    print("No es un triangulo")