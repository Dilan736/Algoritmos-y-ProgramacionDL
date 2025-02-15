Algoritmo comicion_ventas_en_el_mes
	Escribir"Ingresar sueldo base:"
	Leer sueldo_base
	Escribir"Ingresar el valor de la primera venta:"
	Leer venta1
	Escribir"Introduce el valor de la segunda venta:"
	leer venta2
	Escribir"Introduce el valor de la tercera venta:"  
	Leer venta3
	
	comision1=0.10*venta1 
	Comision2=0.10*venta2
	comision3=0.10*venta3
	
	total_comisiones=comision1+comision2+comision3
	Total_Neto_a_recibir=sueldo_base+total_comisiones
	
	Escribir"Total comisiones:",total_comisiones
	Escribir "Total Neto a recibir/sueldo base+cosiones)es:",Total_Neto_a_recibir
FinAlgoritmo
