
categoria = int(input("ingrese su categoria: "))
sueldo= int(input("ingrese sueldo "))

if categoria == 1:
    porcentaje = 0.15
elif categoria == 2:
    porcentaje = 0.10
elif categoria == 3:
    porcentaje = 0.08
elif categoria == 4:
    porcentaje = 0.07
else:
    porcentaje = 0

if porcentaje > 0:
    aumento = sueldo * porcentaje
    nuevo_sueldo = sueldo + aumento
    print(f"Categoría del trabajador: {categoria}")
    print(f"Nuevo sueldo: ${nuevo_sueldo:,.2f}")
else:
    print("Error: La categoría ingresada no es válida.")
    