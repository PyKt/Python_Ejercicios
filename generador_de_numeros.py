import random
from io import open
import pathlib
import string
import time
import datetime

fecha = datetime.datetime.now()
personalizada = fecha.strftime("%H-%M")

arch = open("Resultado.txt", "a+")
arch.write("#####Resultado Nacional#####\n")
for lot in range(3):

    lot = random.randint(1,100)
    arch = open(f"Resultado.txt", "a+")
    arch.write(f"{lot}\n")
    print(lot)

arch.write("#####Resultado Leidsa#####\n")
for led in range(7):

    led = random.randint(1,38)
    arch = open("Resultado.txt", "a+")
    arch.write(f"{led}\n")
    print(led)
arch.closed