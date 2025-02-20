import math
# Entrada
metros = float(input("Ingresar cantidad en metros: "))

# Caja negra: Conversión a pies y pulgadas
pulgadas_total = metros * 39.27
FT = math.trunc(pulgadas_total / 12)
pulgadas_restantes = pulgadas_total - (FT * 12)

# Salidas
print("Cantidad en FT es:", FT)
print("Cantidad en pulgadas es:", pulgadas_restantes)


