import subprocess
## Uso de siclo FOR.
lista = [1,2,3,4,5,6,7,8,9]
for i in lista:
    print(i)

lista = [1,2,3,4,5,6,7,8,9]
recorrido = 0
for recorrido, i in enumerate (lista):
    lista[recorrido]*=10
    print(lista)

for i in range(10):
    print(i)

frase = str(input("Ingrese la frase: "))
diccionario = ('aeiouAEIOUqwhjkdkzxd1234567890')
conter = 0 
for i in frase:
    if diccionario in diccionario:
        conter = conter +1

print("Numero de vocales: ", conter)

multiplo = int(input('ingresa el valor'))
for calc in range(1,11):
    print(f"{multiplo} x {calc} = {multiplo*calc} ")


for numero in range(1,61):
    cuadrado = numero*numero
    print(f"El cuadrado de {numero}es de{cuadrado }")
    print(cuadrado)

def matematicas():
    while True:
        str(input("""INDIQUE EL TIPO DE OPERADOR MATEMATICO:
        [S]Para sumar
        [M]Para multiplicar
        [D]Para dividir
        [R]Para substraer"""))
        operador_uno = float()
        operador_dos = float()
        calc = str()




