pago = int(input('ingresa pago por hora '))
horas = int(input('ingrese las horas trabajadas'))
try:
    salario = pago*horas
    horasextras = horas - 40
    extras = (40*pago) + (horasextras*pago*1.5)
    if horas >= 40 :
        print("El salario es: S/", extras)
    else :
        print("El salario es: S/", salario)
except:
    pago = -1
    horas = -1
    print('error,por favor ingresar numeros')

