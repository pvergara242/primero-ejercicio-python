import json

class Contador:
            def conteo(self,nombre_archivo):
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
                print('Las 10 palabras qué más se repiten son:')
                for _words in sorted(palabras, key=palabras.get, reverse=True)[ :10] :
                    print('\t', _words, ':', palabras[_words], 'Veces')
_filename = input( '"Ingrese el nombre del archivo:" ').strip()
_countDict = Contador()
_countDict.conteo(_filename)