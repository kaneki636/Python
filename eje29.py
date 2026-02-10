# Definimos los datos iniciales
salario_base = float(input("Ingrese el salario mensual de los vendedores: "))

print("\n--- Registro de Ventas por Departamento ---")
ventas_dept1 = float(input("Ventas Departamento 1: "))
ventas_dept2 = float(input("Ventas Departamento 2: "))
ventas_dept3 = float(input("Ventas Departamento 3: "))

total_ventas = ventas_dept1 + ventas_dept2 + ventas_dept3

umbral = total_ventas * 0.33

def calcular_pago(ventas_dept, salario):
    if ventas_dept > umbral:
        return salario + (salario * 0.20)
    else:
        return salario

pago_dept1 = calcular_pago(ventas_dept1, salario_base)
pago_dept2 = calcular_pago(ventas_dept2, salario_base)
pago_dept3 = calcular_pago(ventas_dept3, salario_base)


print(f"Total Global de Ventas: ${total_ventas:,.2f}")
print(f"Umbral de incentivo (33%): ${umbral:,.2f}")
print(f"Pago final Departamento 1: ${pago_dept1:,.2f}")
print(f"Pago final Departamento 2: ${pago_dept2:,.2f}")
print(f"Pago final Departamento 3: ${pago_dept3:,.2f}")