a = int(input("Ingrese un numero (entero, positivo):"))
b = int(input("Ingrese un numero (entero, positivo):"))
c = int(input("Ingrese un numero (entero, positivo):"))
d = int(input("Ingrese un numero (entero, positivo):"))

#entero positivo

n = int(f"{a}{b}{c}{d}")


#condiccion
if n is not None: 
    redondeo = round(n, -2)
    print(f"El número formado es: {redondeo}")