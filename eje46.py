k = int(input("Ingrese un numero positivo de k:"))
n = int(input("Ingrese un numero positivo de n:"))


if n > 0 and k > 0 and k < n:
    print(f"Secuencia desde {n} hasta {k}:")

    while n >= k:
        if n > k:
            print(n, end=", ")
        else:
            print(n) 
            
        n = n - 1
else:
    print("Error: Asegúrese de que N y K sean positivos y que K sea menor que N.")