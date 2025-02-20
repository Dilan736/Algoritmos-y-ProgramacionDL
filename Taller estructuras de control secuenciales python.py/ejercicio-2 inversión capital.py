# Entrada
capital_invertido = int(input("Introducir capital invertido: "))

# Caja negra: cálculo del interés y monto final
interes_mensuales = 0.02 * capital_invertido
monto_final = capital_invertido + interes_mensuales

# Salidas
print("El interés ganado es:", interes_mensuales)
print("Total ganancias después de un mes es:", monto_final)

