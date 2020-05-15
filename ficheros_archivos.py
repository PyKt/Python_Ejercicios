import pathlib
import random
from io import open
import string
import pathlib

"""
Manejo de ficheros en python
"""
#Abrimos el archivo
ruta = str(pathlib.Path().absolute()) + "/factura.txt"
archivo = open(ruta, "a+")



## Escribimos el archivo
archivo.write(f"Estoy escribiendo desde python y pondre una sere de claves: 12\n")

# Cerrar archivo
archivo.close

# Leer contenido
ruta = str(pathlib.Path().absolute()) + "/factura.txt"
archivo = open(ruta, "r")# colocamos la "r" como lectura

#contenido = archivo.read()
#print(contenido)

## Leemos como una lista
leerLita = archivo.readlines()
archivo.close
for lector in leerLita:
    print(lector.center(100))