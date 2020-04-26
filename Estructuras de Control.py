# las estructuras son IF, ELSE & ELIF
alberto = 22
if alberto % 2 == 0:
    print('El resto es 0')
else:
    print(str("al resultado es:\t") + alberto)

frase = str(input(": "))
if frase == "Archlinux":
    print(frase + " Es una distro")
elif frase == "linux":
    print(frase + " Es el sistema operativo")
else:
    print(frase + " Eso es otra cosa.")

final = float(input('Coloque su calificacion'))
if final >= 9:
    print("Nota sobresaliente")
elif final >= 7:
    print("Pasaste")
elif final == 6:
    print("Casi")
else:
    print("No Pasaste")

## siclo While == mientas
usuario = int(input('Coloque el numero para ver que pasa: '))
while usuario <= 9:
    usuario += 4
#    if(usuario == 8):
    print("Bienvenido: ",usuario)