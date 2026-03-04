# Pedimos los dos números al usuario
num_a = int(input("Ingresa el primer número (A): "))
num_b = int(input("Ingresa el segundo número (B): "))

#Calcular suma de divisores de A
suma_a = 0
for i in range(1, (num_a // 2) + 1):
    if num_a % i == 0:
        suma_a = suma_a + i

# Calcular suma de divisores de B 
suma_b = 0
for i in range(1, (num_b // 2) + 1):
    if num_b % i == 0:
        suma_b = suma_b + i


print(f"Suma de divisores de {num_a} es: {suma_a}")
print(f"Suma de divisores de {num_b} es: {suma_b}")

if suma_a == num_b and suma_b == num_a:
    print(f"\n¡Confirmado! {num_a} y {num_b} son números amigos.")
else:
    print(f"\nLo siento, {num_a} y {num_b} NO son números amigos.")