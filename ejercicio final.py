import json

def conteo(nombre_archivo):
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
    for word in palabras:
         print(word, palabras[word])
    # print (json.dumps(palabras, indent=4))
pass
nombre_archivo = input('cual es el nombre del archivo ')
conteo(nombre_archivo)