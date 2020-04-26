lista = []
print('Ingresa 5 numeros')

for i in range(5):
    lista.append(str(input("INGRESA LOS NUMEROS")))

losNumeros = ("Asi se escriben los numeros '{}'").format(lista)
print(losNumeros)
