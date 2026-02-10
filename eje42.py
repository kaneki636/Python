
edad_valor = float(input("Ingrese la edad: "))
tipo_edad = input("¿La edad es en (M)eses o (A)ños?: ").upper()
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))


edad_meses = edad_valor if tipo_edad == 'M' else edad_valor * 12

minimo = 0

if edad_meses <= 1:
    minimo = 13
elif edad_meses <= 6:
    minimo = 10
elif edad_meses <= 12:
    minimo = 11
elif edad_meses <= 60: # Hasta 5 años
    minimo = 11.5
elif edad_meses <= 120: # Hasta 10 años
    minimo = 12.6
elif edad_meses <= 180: # Hasta 15 años
    minimo = 13
else:
    # Mayores de 15 años necesitan distinguir sexo
    sexo = input("Ingrese el sexo (H)ombre o (M)ujer: ").upper()
    if sexo == 'M':
        minimo = 12
    else:
        minimo = 14


if hemoglobina < minimo:
    print(f"Resultado: POSITIVO para Anemia.")
    print(f"Su nivel es {hemoglobina} g%, el mínimo para su rango es {minimo} g%.")
else:
    print(f"Resultado: NEGATIVO (Normal).")