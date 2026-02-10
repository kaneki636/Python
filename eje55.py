suma_total = 0
k = 1
conteo_terminos = 0

# El bucle continúa mientras la suma del PRÓXIMO término no exceda 1000
while True:
    proximo_termino = (k**2 + 1) / k
    
    if (suma_total + proximo_termino) > 1000:
        break  # Si el siguiente término nos hace pasar de 1000, nos detenemos
    
    suma_total += proximo_termino
    conteo_terminos += 1
    k += 1

print(f"Número de términos necesarios: {conteo_terminos}")
print(f"Valor de la sumatoria alcanzado: {suma_total:.2f}")