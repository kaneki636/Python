a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))

deno = (a*e - b*d)

if deno == 0:
    print("la operacion no tiene solucion unica")
else:
    x = (c*e - b*f) / deno
    y = (a*f - c*d) / deno

print(f"X =, {x:.2f}")
print(f"Y =, {y:.2f}")
