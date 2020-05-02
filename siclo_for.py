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
