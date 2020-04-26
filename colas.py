from collections import deque
colas = deque
type(colas)
print(colas)

colas = deque(['Gente', 'Grupos', 'Individuos'])
print(colas)
#A diferecias de las pilas, en las colas puedes usar el atributo popleft
colas.popleft()

print(colas)