
n_cuestionarios = 64
n_preguntas = 23


promedios = []
cont_inf_3 = 0
cont_sup_4 = 0
cont_excelente = 0 

for i in range(1, n_cuestionarios + 1):
    print(f"Instrumento #{i}:")

    pt = float(input(f"  Ingrese la suma total de puntos (entre 23 y 115): "))
    
    promedio = pt / n_preguntas
    promedios.append(promedio)
    
  
    if promedio < 3: cont_inf_3 += 1
    if promedio > 4: cont_sup_4 += 1
    if 4.5 <= promedio <= 5: cont_excelente += 1


p_alto = max(promedios)
p_bajo = min(promedios)
media_general = sum(promedios) / n_cuestionarios


print(f"a. Media General: {media_general:.2f}")
print(f"b. Promedio más alto: {p_alto:.2f} (Instrumento #{promedios.index(p_alto) + 1})")
print(f"c. Promedio más bajo: {p_bajo:.2f} (Instrumento #{promedios.index(p_bajo) + 1})")


if cont_sup_4 > 0:
    print(f"d. Porcentaje <3 respecto a >4: {(cont_inf_3 / cont_sup_4) * 100:.2f}%")


print(f"e. Porcentaje [4.5 - 5] del total: {(cont_excelente / n_cuestionarios) * 100:.2f}%")