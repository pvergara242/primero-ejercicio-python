nombre_archivo = input('Introduce el nombre del archivo: ')
try:
  with open(nombre_archivo) as f_obj:
      contents = f_obj.read()
except FileNotFoundError:
    msg = "parace que el archivo  " +  nombre_archivo  +   "no ha sido encontrado"
    print(msg)
palabras= {}
nuevas_palabras = [palabras.count(p) for p in palabras]
for c in nombre_archivo:
  if c not in palabras:
    palabras[c] = 1
  else:
    palabras[c] = palabras[c] + 1
print(palabras)