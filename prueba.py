def contador():
nombre_archivo = input('cual es el nombre del archivo ')
try:
    fhand = open(nombre_archivo)
except:
    print("el archivo: " + nombre_archivo  + "no ha sido encontrado" )
    exit()

palabras = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in palabras:
            palabras[word] = 1
        else:
            palabras[word] += 1
print(palabras)