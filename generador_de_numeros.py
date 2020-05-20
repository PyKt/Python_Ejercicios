import random
from io import open
import pathlib
import string
import time
import datetime


class Loteria:
    def __init__(self):
        pass

    def juego(self):
        fecha = datetime.datetime.now()
        fechaArchivo = fecha.strftime("El %D a las - %H:%M:%S\n\n")
        arch = open("Resultado.txt", "a+")
        arch.write(f"Creado {fechaArchivo}")
        arch.write("#####Resultado Nacional#####\n")

        for lot in range(3):
            lot = random.randint(1, 100)
            arch = open(f"Resultado.txt", "a+")
            arch.write(f"{lot}\n")
            print(lot)

        arch.write("#####Resultado Leidsa#####\n")

        for led in range(7):
            led = random.randint(1, 38)
            arch = open("Resultado.txt", "a+")
            arch.write(f"{led}\n")
            print(led)
        arch.closed


Resultado = Loteria()
Resultado.juego()