# Variables para contar y sumar (empezamos en 0)
total_empresas = 0
cant_agricolas = 0
cant_mineras_total = 0
cant_mineras_sur = 0

# Para los promedios de trabajadores (una variable por cada actividad)
trabajadores_agricola = 0
trabajadores_industrial = 0
trabajadores_minera = 0
trabajadores_pesquera = 0
trabajadores_otra = 0

cont_agricola = 0
cont_industrial = 0
cont_minera = 0
cont_pesquera = 0
cont_otra = 0

# Para saber cuál localización tiene más industriales
ind_norte = 0
ind_sur = 0
ind_este = 0
ind_oeste = 0

while True:
    print("\n--- Registro de Nueva Empresa ---")
    actividad = int(input("Actividad (1:Agrícola, 2:Industrial, 3:Minera, 4:Pesquera, 5:Otra): "))
    loc = int(input("Localización (1:Norte, 2:Sur, 3:Este, 4:Oeste): "))
    empleados = int(input("Número de trabajadores: "))
    
    total_empresas = total_empresas + 1
    
    # i. Porcentaje de agrícolas
    if actividad == 1:
        cant_agricolas = cant_agricolas + 1
        trabajadores_agricola = trabajadores_agricola + empleados
        cont_agricola = cont_agricola + 1
        
    # ii. Porcentaje mineras del sur
    elif actividad == 2:
        trabajadores_industrial = trabajadores_industrial + empleados
        cont_industrial = cont_industrial + 1
        # iv. Contar industriales por zona
        if loc == 1: ind_norte += 1
        elif loc == 2: ind_sur += 1
        elif loc == 3: ind_este += 1
        elif loc == 4: ind_oeste += 1
        
    elif actividad == 3:
        cant_mineras_total = cant_mineras_total + 1
        trabajadores_minera = trabajadores_minera + empleados
        cont_minera = cont_minera + 1
        if loc == 2:
            cant_mineras_sur = cant_mineras_sur + 1
            
    elif actividad == 4:
        trabajadores_pesquera = trabajadores_pesquera + empleados
        cont_pesquera = cont_pesquera + 1
        
    elif actividad == 5:
        trabajadores_otra = trabajadores_otra + empleados
        cont_otra = cont_otra + 1

    # Preguntar si quiere seguir
    continuar = input("¿Desea registrar otra empresa? (si/no): ")
    if continuar.lower() == "no":
        break


# i. Porcentaje Agrícolas
porc_agricola = (cant_agricolas / total_empresas) * 100
print(f"Porcentaje de empresas agrícolas: {porc_agricola}%")

# ii. Porcentaje Mineras del Sur (evitamos dividir por cero si no hay mineras)
if cant_mineras_total > 0:
    porc_min_sur = (cant_mineras_sur / cant_mineras_total) * 100
    print(f"Porcentaje de mineras que están en el sur: {porc_min_sur}%")

# iii. Promedios (solo si el contador es mayor a 0)
if cont_agricola > 0: print(f"Promedio trabajadores Agrícola: {trabajadores_agricola/cont_agricola}")
if cont_industrial > 0: print(f"Promedio trabajadores Industrial: {trabajadores_industrial/cont_industrial}")
if cont_minera > 0: print(f"Promedio trabajadores Minera: {trabajadores_minera/cont_minera}")
if cont_pesquera > 0: print(f"Promedio trabajadores Pesquera: {trabajadores_pesquera/cont_pesquera}")
if cont_otra > 0: print(f"Promedio trabajadores Otra: {trabajadores_otra/cont_otra}")

# iv. Localización con más industriales (usamos una lógica sencilla de comparación)
max_ind = max(ind_norte, ind_sur, ind_este, ind_oeste)
if max_ind == 0:
    print("No se registraron empresas industriales.")
elif max_ind == ind_norte: print("La zona con más industriales es: Norte")
elif max_ind == ind_sur: print("La zona con más industriales es: Sur")
elif max_ind == ind_este: print("La zona con más industriales es: Este")
elif max_ind == ind_oeste: print("La zona con más industriales es: Oeste")