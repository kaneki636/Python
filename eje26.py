"""26. Dados los datos A, B, C y D que representan números enteros; 
escriba un algoritmo que calcule el resultado de las siguientes expresiones:
Si D=0 (A-C)2
Si D>0 (A-B )3
D"""

#datos 
a = int(input("Ingrese un numero (entero):"))
b = int(input("Ingrese un numero (entero):"))
c = int(input("Ingrese un numero (entero):"))
d = int(input("Ingrese un numero (entero):"))

#condiccion
if d == 0:
    resultado= float (a-c)**2
    print(f" Como D es igual a 0 esto puedo entenderse como: {resultado}")
elif d > 0 :
    nose = ((a-b)**3)/d
    print(f"Como de es menor que o este puede entenderse como: {nose}")
else:
    print("D es menor que o entonces o aplica este caso")