Algoritmo monto_total_a_pagar_luz
	escribir" ingresar lectura del mes anterior:"
	leer lectura_mes_anterior
	escribir"ingresar lectura del mes actual:"
	leer lectura_mes_actual
	Escribir"ingresar el costo por kilovatio:"
	leer costo_por_kilovatio
	consumo_energia=lectura_mes_actual-lectura_mes_anterior
	monto_a_pagar=consumo_energia*costo_por_kilovatio
	Escribir "el consumo de energia es:", consumo_energia,"kilovatios"
	Escribir "el costo total es de:",monto_a_pagar,"unidades monetarias"
FinAlgoritmo
