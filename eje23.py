
M = float(input("Kilogramos de harina obtenidos (M): "))
N = float(input("Litros de aceite obtenidos (N): "))
B1 = float(input("Precio por bulto de harina (B1): "))
B2 = float(input("Precio por caja de aceite (B2): "))
B3 = float(input("Precio de harina al detal (B3): "))
B4 = float(input("Precio de aceite al detal (B4): "))

bultos_harina = M // 24
sobrante_harina = M % 24
ingreso_harina = (bultos_harina * B1) + (sobrante_harina * B3)
cajas_aceite = N // 15
sobrante_aceite = N % 15
ingreso_aceite = (cajas_aceite * B2) + (sobrante_aceite * B4)
total = ingreso_harina + ingreso_aceite


print(f"Resultado del análisis:")
print(f"• Harina: {bultos_harina:.0f} bultos y {sobrante_harina:.2f} kg sueltos.")
print(f"• Aceite: {cajas_aceite:.0f} cajas y {sobrante_aceite:.2f} lt sueltos.")
print(f"• INGRESO TOTAL: Bs. {total:,.2f}")
