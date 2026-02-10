parcial1 = float(input("Nota parcial 1: "))
parcial2 = float(input("Nota parcial 2: "))
parcial3 = float(input("Nota parcial 3: "))
exa_final = float(input("Nota examen final: "))
trabajo_final = float(input("Nota trabajo final: "))

pro_parciales = (parcial1 + parcial2 + parcial3) / 3
nota_final = (pro_parciales * 0.55) + (exa_final * 0.30) + (trabajo_final * 0.15)

print("promedio de los parciales", pro_parciales)
print("nota final", nota_final)