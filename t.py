import random
import string
import subprocess
import threading
import time
import datetime
import os

"""
Proceso de borrado autostart    
"""

print("los numeros al azar")

lista = [12, 21, 55, 18, 91]
lista.sort()
print(lista)

"""
lista = [12,18,11]
lista.extend([12,21,11])
La(lista)
print(lista)

for i in enumerate(lista):
    print(i)
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

print("########Numeros al azar###########")
for i in range(0, 3):
    i = random.randint(1, 100)
    print(i)
stringLength = ''

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

for i in get_random_alphaNumeric_string(13):
    i = get_random_alphaNumeric_string(10)
    print(i)

