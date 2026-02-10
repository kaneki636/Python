CHELIN_PESETA     = 956.871 / 100  
DRACMA_PESETA     = 20.110  / 100  
PESETA_DOLAR      = 1 / 122.499      
PESETA_LIRA       = 100 / 9.289   
PESETA_FRANCO_FRA = 1 / 9.289        

# Chelines austríacos - Pesetas
chelines = float(input("Cantidad en chelines austríacos: "))
pesetas1 = chelines * CHELIN_PESETA
print(f"{chelines:.2f} chelines austríacos = {pesetas1:.2f} pesetas")

# Dracmas griegos - Francos franceses
dracmas = float(input("\nCantidad en dracmas griegos: "))
pesetas2 = dracmas * DRACMA_PESETA
francos_franceses = pesetas2 * PESETA_FRANCO_FRA
print(f"{dracmas:.2f} dracmas griegos = {francos_franceses:.4f} francos franceses")

# Pesetas - Dólares y Liras italianas
pesetas = float(input("\nCantidad en pesetas: "))
dolares = pesetas * PESETA_DOLAR
liras = pesetas * PESETA_LIRA

print(f"{pesetas:,.2f} pesetas equivalen a:")
print(f" {dolares:,.4f} dólares estadounidenses")
print(f" {liras:,.2f} liras italianas")
