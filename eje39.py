
costo = float(input("¿Cuánto valen? "))
depre_anual = float(input("¿Cuánto pierde el auto al año?: "))
subida_anual = float(input("¿Cuánto sube el terreno al año?: "))

valor_auto_final = costo * (1 - depre_anual)**3
devaluacion_auto = costo - valor_auto_final


valor_terreno_final = costo * (1 + subida_anual)**3
incremento_terreno = valor_terreno_final - costo

mitad_incremento = incremento_terreno / 2

if devaluacion_auto <= mitad_incremento:
    print("DECISIÓN: Compra el AUTO")
else:
    print("DECISIÓN: Compra el TERRENO")