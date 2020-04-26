## Las tuplas son elementos inmutables distintos a las listas
import subprocess


tup1 = ('alberto', 'raines', 1986, 1992, [12, 23, 44])
print(tup1[1])
print(tup1[3:])
print(tup1.index('alberto'))
print(tup1.count(44))
print(len(tup1))
print(tup1.count(12))

hack = str(input("""Selecciona el tipo de siclo a usar
1 - Siclo while
2 - Siclo for."""))
if hack == 1:
    hack = hack
    
elif hack == 2:
    hack = hack

while hack == hack:
    print('''Selecciones la Opcion correcta
    1 - Estado del sistema
    2 - Comprobar estado de actualizacion
    3 - Instalar paquetes''')

    attack = int(input())
    if attack == 1:
        subprocess.call(['htop'])
        subprocess.call(['clear'])

    if attack == 2:
        subprocess.call(['yay'])
        subprocess.call(["clear"])

    elif attack == 3:
        pacman = str(input("Ingrese el nombre del paquete: "))
        if pacman == pacman:
            subprocess.call(['sudo', 'pacman', '-S', pacman])                  

for i in hack:
    print('''Seleccione la Opcion correcta
    1 - Estado del sistema
    2 - Comprobar estado de actualizacion
    3 - Instalar paquetes''')
    i = int(input())
    if i == 1:
        subprocess.call(['htop'])
        subprocess.call(['clear'])
    if attack == 2:
        subprocess.call(['yay'])
        subprocess.call(["clear"])

    elif i == 3:
        pacman = str(input("Ingrese el nombre del paquete: "))
        if pacman == pacman:
            subprocess.call(['sudo', 'pacman', '-S', pacman]) 
            subprocess.call(['clear'])