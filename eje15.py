l_anterior = float(input("Lectura anterior: "))
l_actual = float(input("Lectura actual: "))
costo_kw = float(input("Costo por kilovatio: "))

consumo = l_actual - l_anterior
total = consumo * costo_kw

print("Total a pagar:", total)
