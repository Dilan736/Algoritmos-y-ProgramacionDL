# Entrada
calificacion1 = int(input("Ingrese la primera calificación parcial: "))
calificacion2 = int(input("Ingrese la segunda calificación parcial: "))
calificacion3 = int(input("Ingrese la tercera calificación parcial: "))
examen_final = int(input("Ingrese la calificación del examen final: "))
trabajo_final = int(input("Ingrese la calificación del trabajo final: "))

# Caja negra:
promedio_parciales = (calificacion1 + calificacion2 + calificacion3) / 3
calificacion_final = (0.55 * promedio_parciales) + (0.30 * examen_final) + (0.15 * trabajo_final)

# Salidas
print("La calificación final es:", calificacion_final)
