# para asegurarse de que el resultado sea correcto se debe de usar
# entre parentecis.

getPrimero = 10
getSegundo = 25

print(getPrimero * getSegundo - 2 or not (getPrimero % getSegundo) == 0)
print(getPrimero * getSegundo <= 6 or not (getSegundo % getPrimero) == 0)

## Hacemos reasignacion de valores

getValor = 33

print(getValor)

getValor *= 8
print(getValor)

getValor /= 8
print(getValor)

print(getValor == 12)
print(getValor >= 12)
print(getValor <= 12)