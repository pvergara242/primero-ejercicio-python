nombre_archivo = input('Introduce el nombre del archivo: ')
try:
    handler = open(nombre_archivo)
except FileNotFoundError:
    print('Archivo no encontrado:', nombre_archivo)

while(True):
    linea = handler.readline().strip()
    print(linea)
    if not linea:
        break
handler.close()