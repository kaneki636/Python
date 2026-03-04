dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

cociente = 0
# divisiones sucesivas

while dividendo >= divisor:
    dividendo = dividendo - divisor
    cociente +=1
    print (f"Esta es la cantidad de restas secesivas: {cociente}")


