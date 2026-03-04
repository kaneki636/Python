# acumuladores
tachira = 0
distrito = 0
total_huerfanos = 0

edad_grupo1 = 0
edad_grupo2 = 0
edad_grupo3 = 0
edad_grupo4 = 0

nino = 0      # sin tilde para evitar problemas
nina = 0

continuar = "s"

while continuar == "s":
    total_huerfanos += 1

    sexo    = input("Ingrese el sexo (M/F): ")
    edad    = int(input("Ingrese la edad del niño: "))
    orfa    = input("Nombre del orfanatorio: ")
    estado  = input("Estado (Táchira / Distrito Capital / otro): ")


    if estado == "Táchira":
        tachira += 1
    elif estado == "Distrito Capital":
        distrito += 1

    # grupos de edad
    if edad < 1:
        edad_grupo1 += 1
    elif edad <= 3:
        edad_grupo2 += 1
    elif edad <= 6:
        edad_grupo3 += 1
    else:
        edad_grupo4 += 1

    
    if sexo == "M":
        nino += 1
    elif sexo == "F":
        nina += 1

    continuar = input("¿Hay otro niño? (s/n): ").lower()

porcentaje_tachira  = (tachira / total_huerfanos) * 100
porcentaje_distrito = (distrito / total_huerfanos) * 100
print(f"a) Huérfanos en Táchira: {tachira} ({porcentaje_tachira:.2f}%)")
print(f"a) Huérfanos en Distrito Capital: {distrito} ({porcentaje_distrito:.2f}%)")

# inciso b)
print(f"b) Grupo 1 - menores de 1 año: {edad_grupo1}")
print(f"b) Grupo 2 - entre 1 y 3 años: {edad_grupo2}")
print(f"b) Grupo 3 - entre 4 y 6 años: {edad_grupo3}")
print(f"b) Grupo 4 - mayores de 6 años: {edad_grupo4}")

# inciso c)
porcentaje_nino = (nino / total_huerfanos) * 100
porcentaje_nina = (nina / total_huerfanos) * 100
print(f"c) Niños: {nino} ({porcentaje_nino:.2f}%)")
print(f"c) Niñas: {nina} ({porcentaje_nina:.2f}%)")
