horas = float(input("Número de horas trabajadas: "))
valor_hora = float(input("Valor por hora $: "))

salario_base = horas * valor_hora
descuento = salario_base * 0.20
salario_neto = salario_base - descuento

