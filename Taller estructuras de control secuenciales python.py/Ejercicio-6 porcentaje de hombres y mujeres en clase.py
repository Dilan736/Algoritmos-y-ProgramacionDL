# Entrada
total_estudiantes = int(input("Introduce el total de estudiantes en el grupo: "))
num_hombres = int(input("Introduce el número de hombres: "))
num_mujeres = int(input("Introduce el número de mujeres: "))

# Caja negra: Cálculo de los porcentajes
porcentaje_hombres = (num_hombres / total_estudiantes) * 100
porcentaje_mujeres = (num_mujeres / total_estudiantes) * 100

# Salidas
print("El porcentaje de hombres es:", porcentaje_hombres, "%")
print("El porcentaje de mujeres es:", porcentaje_mujeres, "%")

