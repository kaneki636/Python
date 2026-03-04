from datetime import datetime

print("--- REGISTRO DE FACTURA ---")

# 1. Entrada de datos por pantalla
num_fac = input("Número de factura: ")
nom_cli = input("Nombre del cliente: ")
mon_fac = float(input("Monto de la factura: "))
fec_com_str = input("Fecha de compra (DD/MM/AAAA): ")
fec_pag_str = input("Fecha de pago (DD/MM/AAAA): ")


fecha_compra = datetime.strptime(fec_com_str, "%d/%m/%Y")
fecha_pago = datetime.strptime(fec_pag_str, "%d/%m/%Y")
dias = (fecha_pago - fecha_compra).days


interes_mora = 0
monto_descontado = 0

if dias > 60:
    interes_mora = mon_fac * 0.08
elif dias >= 31 and dias <= 59:
    interes_mora = mon_fac * 0.06
elif dias < 15:
    monto_descontado = mon_fac * 0.02


monto_a_cancelar = mon_fac + interes_mora - monto_descontado


print("FACTURA NÚMERO:", num_fac)
print("CLIENTE:", nom_cli)
print("MONTO DE LA FACTURA: $", mon_fac)
print("DÍAS TRANSCURRIDOS:", dias)
print("MONTO POR INTERÉS DE MORA: $", interes_mora)
print("MONTO DESCONTADO: $", monto_descontado)
print("MONTO TOTAL A CANCELAR: $", monto_a_cancelar)
