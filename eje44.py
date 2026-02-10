# 1. Entrada de datos
inversion_total = float(input("¿Cuánto dinero se necesita para el negocio en total?: "))
monto_hipoteca = float(input("¿Cuánto dinero le presta el banco por la hipoteca?: "))


if monto_hipoteca < 1000000:
    # Caso 1: Hipoteca pequeña. Se van 50/50.
    inversion_persona = inversion_total * 0.50
    inversion_socio = inversion_total * 0.50
else:
    # Caso 2: Hipoteca grande. 
    sobrante = inversion_total - monto_hipoteca
    
    if sobrante > 0:
        # Si la hipoteca no alcanzó, el resto se divide entre dos
        inversion_persona = monto_hipoteca + (sobrante / 2)
        inversion_socio = sobrante / 2
    else:
        # Si la hipoteca cubrió todo o más, la persona pone el total y el socio nada
        inversion_persona = inversion_total
        inversion_socio = 0


print(f"Inversión de la Persona: ${inversion_persona:,.2f}")
print(f"Inversión del Socio:   ${inversion_socio:,.2f}")
