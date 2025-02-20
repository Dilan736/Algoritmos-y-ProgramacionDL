#salario y comisiones 
# Entrada
sueldo_base = int(input("Ingresar sueldo base: "))
venta1 = int(input("Ingresar el valor de la primera venta: "))
venta2 = int(input("Introducir el valor de la segunda venta: "))
venta3 = int(input("Introducir el valor de la tercera venta: "))

# Caja negra
comision1 = 0.10 * venta1
comision2 = 0.10 * venta2
comision3 = 0.10 * venta3
total_comisiones = comision1 + comision2 + comision3
total_neto_a_recibir = sueldo_base + total_comisiones

# Salidas
print("Total comisiones:", total_comisiones)
print("Total neto a recibir (sueldo base + comisiones):", total_neto_a_recibir)

