nombre = input("Ingrese el nombre del trabajador: ")
h_normales = float(input("Horas normales trabajadas: "))
p_hora = float(input("Pago por hora normal: "))
h_extras = float(input("Horas extras trabajadas: "))
hijos = int(input("Número de hijos: "))

s_base = h_normales * p_hora
pago_extra = h_extras * (p_hora * 1.25)

asignaciones = 25000 + (17300 * hijos) + 18000
deducciones = s_base * (0.05 + 0.02 + 0.07)

s_neto = s_base + pago_extra + asignaciones - deducciones

print("Asignaciones:", asignaciones)
print("Deducciones:", deducciones)
print("Sueldo neto:", s_neto)
