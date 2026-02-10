metros = float(input("Ingrese la cantidad en metros: "))

pulgadas_totales = metros * 39.27
pies = int(pulgadas_totales // 12)        
pulgadas_restantes = pulgadas_totales % 12

print("metros",metros)
print("pies",pies)
print("pulgadas", pulgadas_restantes)
print("pulgadas en total:", pulgadas_totales)
