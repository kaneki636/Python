total_estudiantes = int(input("¿Cuántos estudiantes hay en total?: "))
hombres = int(input("¿Cuántos son hombres?: "))


mujeres = total_estudiantes - hombres
porc_hombres = (hombres / total_estudiantes) * 100
porc_mujeres = (mujeres / total_estudiantes) * 100

print("Total estudiantes:", total_estudiantes)
print("Porcentaje hombres", porc_hombres)
print("Porcentaje mujeres", porc_mujeres)