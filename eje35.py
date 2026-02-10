Nombre = input("Ingrese su nombre : ")
temperatura = int(input("Ingrese su temperatura: "))



if temperatura >= 85:
    
    totalPagar = temperatura
    print("Eres apto para natacion")

elif 70 < temperatura <= 85:
    
    print(f"Eres apto para tenis", )
    
elif 32 < temperatura <= 70:
    
    
    print(f"Eres apto para golf")

elif 10 < temperatura <= 32:
    
   
    print(f"Eres apto para Esqui")

else:
    
    temperatura <= 10
    print(f"Eres apto para Marcha")

