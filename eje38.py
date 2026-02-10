from datetime import datetime

fecha = int(input("Ingrese su fecha de nacimiento (dd/mm/año): "))

partes = fecha.split("/")
dia = int(partes[0])
mes = int(partes[1])
anio = int(partes[2])


hoy = datetime.now()
dia_actual = hoy.day
mes_actual = hoy.month
anio_actual = hoy.year

edad = anio_actual - anio

if mes_actual < mes:
    edad = edad - 1
elif mes_actual == mes:
    if dia_actual < dia:
        edad = edad - 1

if mes == 1:
    if dia >= 21:
        signo = "Acuario"
    else:
        signo = "Capricornio"
elif mes == 2:
    if dia >= 20:
        signo = "Piscis"
    else:
        signo = "Acuario"
elif mes == 3:
    if dia >= 21:
        signo = "Aries"
    else:
        signo = "Piscis"
elif mes == 4:
    if dia >= 21:
        signo = "Tauro"
    else:
        signo = "Aries"
elif mes == 5:
    if dia >= 22:
        signo = "Géminis"
    else:
        signo = "Tauro"
elif mes == 6:
    if dia >= 22:
        signo = "Cáncer"
    else:
        signo = "Géminis"
elif mes == 7:
    if dia >= 23:
        signo = "Leo"
    else:
        signo = "Cáncer"
elif mes == 8:
    if dia >= 24:
        signo = "Virgo"
    else:
        signo = "Leo"
elif mes == 9:
    if dia >= 23:
        signo = "Libra"
    else:
        signo = "Virgo"
elif mes == 10:
    if dia >= 23:
        signo = "Escorpión"
    else:
        signo = "Libra"
elif mes == 11:
    if dia >= 22:
        signo = "Sagitario"
    else:
        signo = "Escorpión"
elif mes == 12:
    if dia >= 22:
        signo = "Capricornio"
    else:
        signo = "Sagitario"

# 5. Salida de resultados
print("\n--- Resultados ---")
print("Signo del zodiaco:", signo)
print("Edad actual:", edad, "años")
