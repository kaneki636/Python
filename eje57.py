
n = int(input("Ingrese su numero para calcular la raiz:"))

while n<=0:
    print("El numero debe ser positivo")
    print(input("Ingrese el numero:"))

x = 0.1
rn = ((x+n/x)/2)

contador = 0

#condiccion

while abs (x - rn) >= 0.000001:
    x = rn
    rn = ((x+n/x)/2)
    contador += 1

print(f"la raiz de {n} es: {rn}")
print(f"Se necesitaron {contador} iteraciones")

