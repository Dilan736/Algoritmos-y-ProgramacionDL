def salario_trabajador():
    # Entradas
    horas_trabajadas = float(input("Ingresar el número de horas trabajadas: "))
    precio_por_hora = float(input("Ingresar el precio por hora: "))

    # Caja negra
    salario_base = horas_trabajadas * precio_por_hora
    descuento = salario_base * 0.20
    total_salario = salario_base - descuento

    # Salidas
    print(f"El salario base es: {salario_base}")
    print(f"Descuento por impuesto: {descuento}")
    print(f"Total salario es: {total_salario}")

# Llamar a la función
salario_trabajador()
