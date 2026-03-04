def sistema_demografico():
    # Datos iniciales
    poblacion_total_pais = float(input("Ingrese la población total del país: "))
    n_estados = 5
    estados = []
    
    total_poblacion_5_estados = 0
    
    # Variables para el mayor y menor
    max_poblacion = -1
    nombre_max = ""
    min_poblacion = float('inf') # Se inicializa con un valor infinito
    nombre_min = ""

    for i in range(n_estados):
        nombre_estado = input(f"\nNombre del Estado {i+1}: ")
        m_municipios = int(input(f"Cantidad de municipios en {nombre_estado}: "))
        
        poblacion_estado = 0
        
        for j in range(m_municipios):
            hab = int(input(f"  Habitantes en municipio {j+1}: "))
            poblacion_estado += hab
        
        # Acumular para el total general de los 5 estados
        total_poblacion_5_estados += poblacion_estado
        
        # Determinar el mayor
        if poblacion_estado > max_poblacion:
            max_poblacion = poblacion_estado
            nombre_max = nombre_estado
            
        # Determinar el menor
        if poblacion_estado < min_poblacion:
            min_poblacion = poblacion_estado
            nombre_min = nombre_estado

    # Cálculos finales
    porcentaje = (total_poblacion_5_estados / poblacion_total_pais) * 100
    promedio = total_poblacion_5_estados / n_estados

    # Resultados
    print("\n" + "="*30)
    print("      RESULTADOS FINALES")
    print("="*30)
    print(f"a. Estado con mayor población: {nombre_max} ({max_poblacion} habs.)")
    print(f"b. Estado con menor población: {nombre_min} ({min_poblacion} habs.)")
    print(f"c. Porcentaje respecto al total del país: {porcentaje:.2f}%")
    print(f"d. Promedio de habitantes por Estado: {promedio:,.2f}")

sistema_demografico()