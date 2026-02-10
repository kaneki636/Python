cliente = input("Ingrese el nombre del cliente: ")
compra = int(input("Ingrese el precio de su compra: "))
descuento1 = int (compra * 0.05)
descuento2 = int (compra * 0.11)
descuento3 = int (compra * 0.18)


if compra <= 500:
    
    totalPagar = compra
    print(cliente, "No tienes descuento")

elif 500 < compra <= 1000:
    
    totalPagar1= compra - descuento1
    print(f"Su total a pagar", totalPagar1)
    
elif 1000 < compra <= 7000:
    
    totalPagar2= compra - descuento2
    print(f"Su total a pagar", totalPagar2)
    
else:
    
    7000 < compra <= 15000
    totalPagar3= compra - descuento3
    print(f"Su total a pagar", totalPagar3)

