def sistema_libreria():
    autores = []
    
    # Variables generales
    total_libros = 0
    total_ciencia_ficcion = 0
    total_romance = 0
    
    max_libros_autor = -1
    apellido_autor_max_libros = ""

    # Simulación de entrada de datos
    n_autores = int(input("Ingrese la cantidad de autores: "))

    for i in range(n_autores):
        apellido = input(f"\nApellido del autor {i+1}: ")
        n_libros = int(input(f"¿Cuántos libros ha escrito {apellido}?: "))
        
        # Variables por autor
        suma_paginas_autor = 0
        max_paginas_libro = -1
        codigo_libro_max = ""
        
        # Actualizar autor con más libros (General)
        if n_libros > max_libros_autor:
            max_libros_autor = n_libros
            apellido_autor_max_libros = apellido

        for j in range(n_libros):
            print(f"  Datos del libro {j+1}:")
            codigo = input("    Código: ")
            genero = input("    Género (ciencia ficción, romance, accion, terror, novela, autoayuda, academico): ").lower()
            paginas = int(input("    Número de páginas: "))

            # Cálculos por autor
            suma_paginas_autor += paginas
            if paginas > max_paginas_libro:
                max_paginas_libro = paginas
                codigo_libro_max = codigo
            
            # Cálculos generales
            total_libros += 1
            if genero == "ciencia ficción" or genero == "ciencia ficcion":
                total_ciencia_ficcion += 1
            elif genero == "romance":
                total_romance += 1

        # Mostrar resultados por autor
        print(f"\n--- Reporte Autor: {apellido} ---")
        print(f"Total de páginas escritas: {suma_paginas_autor}")
        print(f"Libro con más páginas: Código {codigo_libro_max} ({max_paginas_libro} págs.)")

    # Cálculos finales generales
    porcentaje_cf = (total_ciencia_ficcion / total_libros * 100) if total_libros > 0 else 0
    cant_cf_romance = total_ciencia_ficcion + total_romance

    # Mostrar resultados generales
    print("\n================================")
    print("       REPORTE GENERAL")
    print("================================")
    print(f"Porcentaje de libros de Ciencia Ficción: {porcentaje_cf:.2f}%")
    print(f"Cantidad total de libros (CF + Romance): {cant_cf_romance}")
    print(f"Autor con más libros: {apellido_autor_max_libros} ({max_libros_autor} libros)")

# Ejecutar el programa
sistema_libreria()