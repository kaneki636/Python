Sbase = float(input("Ingrese el suedo base"))
if (Sbase<400000):
    bono = Sbase*0.15
    Stotal= Sbase+bono
    print("El sueldo total de empleado es", Stotal)
    print("El bono del empleado es:", bono)
else:
    bono=Sbase*0.12
    Stotal=Sbase+bono
    print("El sueldo total del empleado es:", Stotal)
    print("El bono del empleado: ", bono)
    