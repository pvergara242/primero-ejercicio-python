valores = []
valores = (input('ingrese los valores'))
def promedio(valores):
	sumaParcial=0
	for valor in valores:
		sumaParcial+=valor
	cantidadValores = len(valores)
	return sumaParcial/ float(cantidadValores)
print(promedio(valores))