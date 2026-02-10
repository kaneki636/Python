
capital = float(input("Monto del préstamo (X): "))
intereses_pagados = float(input("Total de intereses pagados (Y): "))
tiempo = 4  

razon = (intereses_pagados * 100) / (capital * tiempo)

print("La tasa de interés anual cobrada fue del:", razon, "%")