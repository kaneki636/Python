total_encuestados = 0

# Para edades y géneros
suma_edad_mujeres = 0
cont_mujeres = 0
suma_edad_hombres = 0
cont_hombres = 0

# Para estado civil 1:Soltero, 2:Casado, 3:Otro)
cont_solteros = 0
cont_casados = 0
cont_otros_civil = 0

# Para especialidad 1:Sistemas, 2:Derecho, 3:Administración
cont_esp1 = 0
cont_esp2 = 0
cont_esp3 = 0

# Para rangos de edad específicos
mujeres_adultas = 0  # > 21 años
hombres_jovenes = 0  # < 21 y > 17 años

# Para solteros por género
hombres_solteros = 0
mujeres_solteras = 0

while True:
    edad = int(input("Edad: "))
    sexo = input("Sexo (H/M): ").upper()
    estado_civil = int(input("Estado Civil (1:Soltero, 2:Casado, 3:Otro): "))
    especialidad = int(input("Especialidad (1:Sistemas, 2:Derecho, 3:Admin): "))
    
    total_encuestados += 1
    
    if sexo == "H":
        cont_hombres += 1
        suma_edad_hombres += edad
        if 17 < edad < 21:
            hombres_jovenes += 1
        if estado_civil == 1:
            hombres_solteros += 1
            
    elif sexo == "M":
        cont_mujeres += 1
        suma_edad_mujeres += edad
        if edad > 21:
            mujeres_adultas += 1
        if estado_civil == 1:
            mujeres_solteras += 1

    # Conteo de Estado Civil general
    if estado_civil == 1: cont_solteros += 1
    elif estado_civil == 2: cont_casados += 1
    else: cont_otros_civil += 1
    
    # Conteo de Especialidades
    if especialidad == 1: cont_esp1 += 1
    elif especialidad == 2: cont_esp2 += 1
    elif especialidad == 3: cont_esp3 += 1

    continuar = input("¿Registrar otro alumno? (s/n): ").lower()
    if continuar == 'n':
        break


# a y b promedios de edad
if cont_mujeres > 0:
    print(f"a. Promedio edad mujeres: {suma_edad_mujeres / cont_mujeres:.2f}")
if cont_hombres > 0:
    print(f"b. Promedio edad hombres: {suma_edad_hombres / cont_hombres:.2f}")

# c. Cantidades por sexo
print(f"c. Hombres encuestados: {cont_hombres} | Mujeres encuestadas: {cont_mujeres}")

# d. Porcentaje estado civil respecto al total
print(f"d. Porcentaje Solteros: {(cont_solteros/total_encuestados)*100}%")
print(f"   Porcentaje Casados: {(cont_casados/total_encuestados)*100}%")

# e. Cantidad y porcentaje por especialidad
print(f"e. Especialidad 1: {cont_esp1} ({(cont_esp1/total_encuestados)*100}%)")
print(f"   Especialidad 2: {cont_esp2} ({(cont_esp2/total_encuestados)*100}%)")
print(f"   Especialidad 3: {cont_esp3} ({(cont_esp3/total_encuestados)*100}%)")

# f. Porcentaje mujeres adultas (>21)
print(f"f. Porcentaje mujeres adultas: {(mujeres_adultas/total_encuestados)*100}%")

# g. Porcentaje hombres jóvenes (17 < edad < 21)
print(f"g. Porcentaje hombres jóvenes: {(hombres_jovenes/total_encuestados)*100}%")

# h. Solteros por género
print(f"h. Hombres solteros: {hombres_solteros} | Mujeres solteras: {mujeres_solteras}")