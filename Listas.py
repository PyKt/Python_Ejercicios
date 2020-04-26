# Las listas son un cojunto de mas de un elemento.

getLista: list = [5, 9, "Linux", -8, "ArchLinux"]
getLista.append(+5)  # Agregara el numero 5 al ser una lista mixta.

GetList = getLista[0:]
print(GetList)

GetListNum: list = [1, 2, 3, 4, 5]
GetListNum.append(+20)  # agragara el numero 20 a la lista
print(GetListNum)

GetAlfaBeto: list = ['A', 'B', 'C', 'D']
print(GetAlfaBeto)
GetAlfaBeto[:2] = ['Z', 'R'] #al usar esta orden lo que hace es sustituir los dos primero elementos
print(GetAlfaBeto)

#Una lista anidada se expresaria de esta manera.
Get1 = [1, 2, 3]
Get2 = [4, 5, 6]
Get3 = [7, 8, 9]
GetAnidadas = [Get1, Get2, Get3]
print(GetAnidadas)
