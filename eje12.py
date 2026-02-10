# Matemática
ex_mate = float(input("Examen de Matemática: "))
t1 = float(input("Tarea 1: "))
t2 = float(input("Tarea 2: "))
t3 = float(input("Tarea 3: "))
prom_tareas_m = (t1 + t2 + t3) / 3
prom_mate = ex_mate * 0.90 + prom_tareas_m * 0.10

# Física
ex_fis = float(input("Examen de Física: "))
t1 = float(input("Tarea 1: "))
t2 = float(input("Tarea 2: "))
prom_tareas_f = (t1 + t2) / 2
prom_fis = ex_fis * 0.80 + prom_tareas_f * 0.20

# Química
ex_quim = float(input("Examen de Química: "))
t1 = float(input("Tarea 1: "))
t2 = float(input("Tarea 2: "))
t3 = float(input("Tarea 3: "))
prom_tareas_q = (t1 + t2 + t3) / 3
prom_quim = ex_quim * 0.85 + prom_tareas_q * 0.15

prom_general = (prom_mate + prom_fis + prom_quim) / 3

print("Promedio Matemática:", prom_mate)
print("Promedio Física:", prom_fis)
print("Promedio Química:", prom_quim)
print("Promedio general:", prom_general)
