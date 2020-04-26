import subprocess

def tabla():
    for x in range(11):
        print("7 * {} = {}".format(x,x*7))

"""tabla()# de esta manera llamamos a la funcion         """
"""                                                      """
""" Estos son los argumentos de una funciones en python  """
"""                                                      """

def funcionDos(a,b):
    return a/b

print(funcionDos(b=9,a=10))

def gumFusion(x=None,i=None):
    if x == None or i == None:
        print('Ingrese los numeros')
        return
    return x/i
gumFusion()
gumFusion(12, 12)


"""#            PARTE DOS ARGUMENTOS POR VALOR(REFERENCIAS Y PARAMETROS)               """
"""#      Pasar argumentos por valor o referencia en python las variables dentro       """
"""# de una funcion no es modificada fuera de ella mas las listas si son modificables  """

def studiante(valor):
    valor*=3

print(studiante(valor=3))## Devolvera un None porque esta no puede ser modificada fuera del bloque de codigo

def listax(numeros):
    for x,i in enumerate(numeros):
        numeros[x] *= 3

ListNum = [10,200,3000]
listax(ListNum)

"""Separar elementos de una lista"""

lista = [12,18,25,86,88,54,14] #Creamos la lista que usaremos

def separar_listas(lista_separadas):
    lista_separadas.sort()## Al pasarle el metodo .sort() hacemos que el resultaso salga de menor a mayor
    pares = []
    impares = []
    for i in lista_separadas:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

pares, impares = separar_listas(lista)
print(pares)
print(impares)

"""      Las  funciones integradas son las que se reutilizan  en si mismas  """

def conteo(segundos):
    segundos -= 1
    if segundos >=0:
        print(segundos)
        conteo(segundos)
    else:
        print("Saliste del grupo")

conteo(10)
