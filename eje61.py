# 1. Entrada de datos
multiplicador = int(input("Ingrese el multiplicador: "))
multiplicando = int(input("Ingrese el multiplicando: "))

num1 = multiplicador
num2 = multiplicando

suma_total = 0

print("\nProceso:")
print(f"Multiplicador | Multiplicando")
print("-" * 30)

# 2. Ciclo de cálculo
while multiplicador >= 1:
    # Si el multiplicador es impar, sumamos el multiplicando
    if multiplicador % 2 != 0:
        suma_total = suma_total + multiplicando
        marca = "<- (Es impar, se suma)"
    else:
        marca = ""
    
    # Mostramos el paso actual
    print(f"{multiplicador:^13} | {multiplicando:^13} {marca}")
    
    # El multiplicador se divide entre 2 (división entera //)
    multiplicador = multiplicador // 2
    
    # El multiplicando se duplica
    multiplicando = multiplicando * 2

print(f"El resultado de {num1} x {num2} es: {suma_total}")