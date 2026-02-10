#compras de varias piezas

cantidad_piezas1 = int(input("Ingrese la cantidad de piezas que adquirieron: "))
precio_piezas = float(input("Ingrese el valor de las piezas: "))

#monto total
monto_total = cantidad_piezas1 * precio_piezas
print(f" Su monto total de la compra es {monto_total:.2f}")

#condiccion
if monto_total>500000: 
    invertir_dinero= monto_total * 0.55
    presta_banco = monto_total * 0.30
    credito_fabrica = monto_total * 0.15
elif monto_total<500000:
    invertir_dinero=   monto_total * 0.70
    presta_banco = 0
    credito_fabrica= monto_total *0.30
#intereses 20%
intereses = credito_fabrica * 0.20

print("-" * 40)
print(f"Inversion de sus propios fondos:{invertir_dinero}")
print(f"Su cantidad a pagar de creditos es: {presta_banco}")
print(f"Monto a pagar por intereses: {intereses}")
print(f"Crédito con el fabricante:  ${credito_fabrica:,.2f}")
print(f"Total a pagar con intereses: {monto_total + intereses:,.2f}")
