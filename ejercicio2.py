pago = int(input("Ingrese el pagp por horas"))
horas = int(input("Ingrese las horas trabajadas"))

salario = pago * horas
horasextras = horas - 40
extras = (40 * pago) +(horasextras * pago * 1.5)
if horas >= 40:
 print("El salario es: S/",extras)
else:
 print ("El salario es: S/",salario)