import subprocess
import math
import random
import threading
import string
import time
from io import open
import pathlib
from modulocoche import Coche
from tkinter import Tk

ventana = Tk()
ventana.title("Prueba")

"""
Generador automatico de contraseñas.
"""


def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


for i in get_random_alphaNumeric_string(13):
    i = get_random_alphaNumeric_string(10)
    print(i)

print("########Numeros al azar###########")
for rs in range(0, 3):
    rs = random.randint(1, 100)
    print(rs)

"""
Multi threading
"""


def print_hello():
    for i in range(4):
        time.sleep(0.5)
        print("Hello")


def print_hi():
    for i in range(4):
        time.sleep(0.7)
        print("Hi")


t1 = threading.Thread(target=print_hello)
t2 = threading.Thread(target=print_hi)
t1.start()
t2.start()

"""
Ecuaciones matematicas
"""

print('Imprimimos el valor de pi', math.pi)
print('La Raiz cuadrada de un numero', math.sqrt(20))
print("Redondeo de numero: ", math.floor(32.12832039))