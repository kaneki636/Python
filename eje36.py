cantidad = float(input("Ingrese la cantidad a convertir: "))

if cantidad >=50000:
    billete_50mil = cantidad // 50000
    cantidad = cantidad % 50000
    print(f"Billetes de 50.000: {billete_50mil}")

if cantidad >=20000:
    billete_20mil = cantidad // 20000
    cantidad = cantidad % 20000
    print(f"Billetes de 20.000: {billete_20mil}")

if cantidad >=10000:
    billete_10mil = cantidad // 10000
    cantidad = cantidad % 10000
    print(f"Billetes de 10.000: {billete_10mil}")
    
if cantidad >=5000:
    billete_5mil = cantidad // 5000
    cantidad = cantidad % 5000
    print(f"Billetes de 5.000: {billete_5mil}") 
    
if cantidad >=2000:
    billete_2mil = cantidad // 2000
    cantidad = cantidad % 2000
    print(f"Billetes de 2.000: {billete_2mil}")

if cantidad >=1000:
    billete_1mil = cantidad // 1000
    cantidad = cantidad % 1000
    print(f"Billetes de 1.000: {billete_1mil}") 

if cantidad >=500: 
    billete_500 = cantidad // 500
    cantidad = cantidad % 500
    print(f"Billetes de 500: {billete_500}")    

if cantidad >=100:
    billete_100 = cantidad // 100
    cantidad = cantidad % 100
    print(f"Billetes de 100: {billete_100}")
    
if cantidad >=50:
    billete_50 = cantidad // 50
    cantidad = cantidad % 50
    print(f"Billetes de 50: {billete_50}")
