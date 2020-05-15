"""
Manejo de ficheros en python
"""
ruta = str(pathlib.Path().absolute()) + "/factura.txt"
archivo = open(ruta, "a+")

## Escribimos el archivo
archivo.write(f"Estoy escribiendo desde python y pondre una sere de claves{get_random_alphaNumeric_string(i)}")
