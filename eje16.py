area_lamina = 4 * 1.5
consumo_pieza = 0.5

piezas = int(area_lamina // consumo_pieza)
desperdicio = area_lamina - (piezas * consumo_pieza)

print("Piezas fabricadas:", piezas)
print("Desperdicio:", desperdicio)
