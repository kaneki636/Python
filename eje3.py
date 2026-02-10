sueldo = int(input("cual es el sueldo base?:"))
venta1 = int(input("Valor venta1:"))
venta2 = int(input("Valor venta2:"))
venta3 = int(input("Valor venta3:"))

total = venta1+venta2+venta3
comision = total*0.10
s_total= sueldo+comision

print("Su sueldo con su respectiva comision es:",s_total)