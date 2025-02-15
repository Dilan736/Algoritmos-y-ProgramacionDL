Algoritmo salario_trabajador
	Escribir"ingresar el numero de horas trabajadas:"
	Leer horas_trabajadas
	Escribir "ingresar el preciopor hora:"
	leer precio_por_hora
	salario_base=horas_trabajadas*precio_por_hora
	descuento=salario_base*0.20
	total_salario=salario_base-descuento
	Escribir"el salario base es:",salario_base
	Escribir "descuento por impuesto:",descuento
	Escribir "total salario es:",total_salario
FinAlgoritmo
