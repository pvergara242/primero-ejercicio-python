#escribe un programa que solicite al usuario cuantas horas y el pago por hora para calcular el
#pago del sueldo de un trabajador

horas = int(input("¿Cuantas horas trabajo? "))
pagoHora =float(input("¿Cuanto es el pago por hora? "))
valor = horas * pagoHora
print('el sueldo del trabajador es: ' , valor)