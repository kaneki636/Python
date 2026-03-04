# acumuladores
total_alumnos = 0
nota_menor_prog = None      # ← None, no -1
presentes_ingles = 0
ausentes_ingles = 0
aprobaron_todo = 0
suma_prog = 0               # ← nombre consistente
presentes_prog = 0
presentes_mate = 0
reprobaron_mate = 0

continuar = "s"

while continuar == "s":
    total_alumnos += 1

    # notas
    nota_mate     = float(input("Ingrese nota de Matemática (-1 si no presentó): "))
    nota_prog     = float(input("Ingrese nota de Programación (-1 si no presentó): "))
    nota_in       = float(input("Ingrese nota de Inglés (-1 si no presentó): "))

    # inciso a) nota menor de programación
    if nota_prog != -1:
        presentes_prog += 1
        suma_prog += nota_prog                          # ← nombre consistente
        if nota_menor_prog is None or nota_prog < nota_menor_prog:
            nota_menor_prog = nota_prog                 # ← nombre consistente

    # inciso b) ausentes inglés
    if nota_in == -1:
        ausentes_ingles += 1
    else:
        presentes_ingles += 1

    # inciso c) aprobaron todo
    if nota_mate != -1 and nota_mate >= 6 and \
       nota_prog != -1 and nota_prog >= 6 and \
       nota_in   != -1 and nota_in   >= 6:
        aprobaron_todo += 1

    # inciso e) reprobaron matemática
    if nota_mate != -1:
        presentes_mate += 1                             # ← indentación correcta
        if nota_mate < 6:
            reprobaron_mate += 1

    continuar = input("\n¿Hay otro alumno? (s/n): ").lower()


if nota_menor_prog is not None:
    print(f"a) Nota menor de Programación: {nota_menor_prog:.2f}")
else:
    print("a) Ningún alumno rindió Programación")

if presentes_ingles > 0:
    porcentaje_ausentes = (ausentes_ingles / presentes_ingles) * 100
    print(f"b) Porcentaje de ausentes en Inglés: {porcentaje_ausentes:.2f}%")
else:
    print("b) Ningún alumno presentó Inglés")

print(f"c) Alumnos que aprobaron todo: {aprobaron_todo}")

if presentes_prog > 0:
    promedio_prog = suma_prog / presentes_prog
    print(f"d) Promedio en Programación: {promedio_prog:.2f}")
else:
    print("d) Ningún alumno rindió Programación")

if presentes_mate > 0:
    porcentaje_reprobaron = (reprobaron_mate / presentes_mate) * 100
    print(f"e) Porcentaje que reprobó Matemática: {porcentaje_reprobaron:.2f}%")
else:
    print("e) Ningún alumno rindió Matemática")