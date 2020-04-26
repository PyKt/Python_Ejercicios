import subprocess

class FunsionesSistema:
    memorySystem = subprocess.call(['htop'])
    linuxVers = subprocess.call(['uname','-r'])
    updateSystem = subprocess.call(['sudo','pacman','-Syyuu'])

    def __init__(self):
        pass

    def ram(self):
        memorySystem = True
        if memorySystem == True:
            subprocess.call(['htop'])
            
    def kernel_chec(self):
        linuxVers = True
        if linuxVers == True:
            print('La version de Linux es:\n')
            subprocess.call(['uname', '-r'])

    def system_update(self):
        updateSystem = True
        if updateSystem == True:
            subprocess.call(['sudo ', 'pacman', '-Syyuu'])


poo = FunsionesSistema()

"""

version()

nombre = None
try:
    nombre = int(input('Dime un numero:'))
except ValueError:
    print("debes usar solo Numeros")
except Exception as x:
    print(type (x).__name__)

finally:
    restul = nombre
    print("el numero es: ", restul)

"""