# acumuladores
fuerza_menor    = None
fuerza_mayor    = None
suma_fuerza     = 0
total_satelites = 0
masa_mayor      = None
suma_masas      = 0
altura_menor    = None
altura_mayor    = None

# constantes
G = 6.67259e-11
M = 5.97e24

continuar = "s"

while continuar == "s":
    total_satelites += 1

    nombre = input("Nombre del satélite: ")
    pais   = input("País: ")
    m      = float(input("Masa (Kg): "))
    r      = float(input("Altura (m): "))

    
    F = (G * m * M) / (r ** 2)

    # mayor y menor fuerza
    if fuerza_mayor is None or F > fuerza_mayor:
        fuerza_mayor = F
    if fuerza_menor is None or F < fuerza_menor:
        fuerza_menor = F

    # sumas para promedios
    suma_fuerza += F
    suma_masas  += m

    # mayor masa
    if masa_mayor is None or m > masa_mayor:
        masa_mayor = m

    # mayor y menor altura
    if altura_mayor is None or r > altura_mayor:
        altura_mayor = r
    if altura_menor is None or r < altura_menor:
        altura_menor = r

    continuar = input("¿Hay otro satélite? (s/n): ").lower()

# resultados
if total_satelites > 0:
    print(f"a) Fuerza mayor: {fuerza_mayor:.4f} N")
    print(f"a) Fuerza menor: {fuerza_menor:.4f} N")

    promedio_fuerza = suma_fuerza / total_satelites   # ✅
    print(f"b) Fuerza promedio: {promedio_fuerza:.4f} N")

    print(f"c) Mayor masa: {masa_mayor:.2f} Kg")

    promedio_masa = suma_masas / total_satelites       # ✅
    print(f"d) Masa promedio: {promedio_masa:.2f} Kg")

    print(f"e) Altura menor: {altura_menor:.2f} m")
    print(f"e) Altura mayor: {altura_mayor:.2f} m")

else:
    print("No se ingresaron datos")