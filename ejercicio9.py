valores=[]
cantidadValores
for x in range(3):
    sumaParcial += valores
    cantidadValores = len(valores)
    return sumaParcial/float(cantidadValores)
print(promedio(valores))
