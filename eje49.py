
respuestas = [
    [True, True, True],   
    [True, False, True],  

]

# Iniciamos los contadores
a = b = c = d = e = f = g = h = 0

for p1, p2, p3 in respuestas:
    if p1 and p2 and p3:
        a += 1
    if p1 and p2 and not p3:
        b += 1
    if p1 and not p2 and p3:
        c += 1
    if not p1 and p2 and p3:
        d += 1
    if p1:
        e += 1
    if p2:
        f += 1
    if p3:
        g += 1

    if not p1 and not p2 and not p3:
        h += 1


print(f"a. Tres correctas: {a}")
print(f"b. Solo 1ra y 2da: {b}")
print(f"c. Solo 1ra y 3ra: {c}")
print(f"d. Solo 2da y 3ra: {d}")
print(f"e. Al menos la 1ra: {e}")
print(f"f. Al menos la 2da: {f}")
print(f"g. Al menos la 3ra: {g}")
print(f"h. Ninguna correcta: {h}")