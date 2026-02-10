
X = float(input("Cantidad de naranjas (X): "))
Y = float(input("Precio por docena (Y): "))
K = float(input("Monto total obtenido de la venta (K): "))

docenas = X / 12
inversion = docenas * Y
ganancia_dinero = K - inversion
porcentaje_ganancia = (ganancia_dinero * 100) / inversion


print(f"La ganancia obtenida es del: {porcentaje_ganancia}%")