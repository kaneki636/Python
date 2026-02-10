a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("lados del triangulo", a,b,c)
print("perimetro:",p)
print("Area:", area)
