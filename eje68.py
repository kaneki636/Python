cantidad_encontrados = 0
numero_a_probar = 2  

print("Buscando los 3 primeros números perfectos...")

# El ciclo sigue hasta que encontremos 3 números perfectos
while cantidad_encontrados < 3:
    suma_divisores = 0
    
    # Buscamos los divisores de 'numero_a_probar'
    # Probamos desde 1 hasta la mitad del número y un divisor no puede ser mayor a su mitad
    for i in range(1, (numero_a_probar // 2) + 1):
        if numero_a_probar % i == 0:
            suma_divisores = suma_divisores + i
            
    # Verificamos si es perfecto
    if suma_divisores == numero_a_probar:
        cantidad_encontrados = cantidad_encontrados + 1
        print(f"Número perfecto #{cantidad_encontrados} encontrado: {numero_a_probar}")
        print(f"   (Sus divisores suman: {suma_divisores})")
        
    # Pasamos al siguiente número para seguir probando
    numero_a_probar = numero_a_probar + 1

print("\n¡Búsqueda finalizada!")