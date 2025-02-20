# Entrada
total_compra = float(input("Total de la compra: "))

# Caja negra
descuento = 0.15 * total_compra
total_a_pagar = total_compra - descuento

# Salidas
print("El descuento es de:", descuento)
print("Total a pagar con el descuento incluido es de:", total_a_pagar)
