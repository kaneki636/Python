pvp = float(input("Ingrese el precio original (PVP): "))
p_pagado = float(input("Ingrese el precio pagado: "))

descuento = ((pvp - p_pagado) / pvp) * 100

print("Porcentaje de descuento:", descuento, "%")
