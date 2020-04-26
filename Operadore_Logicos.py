# Para hacer las evaluaciones en las estructuras tenermos los operadores
# Logicos Not, And, Or.
archlinux = not False == True
print(archlinux)

numero = 10
conclusion = numero > 5 and numero < 15 #Con esto comprobamos que si la sentencia es verdadera
print(conclusion)

valorOsi = True or False# Siempre sera verdadero si una de las dos condicionales es verdadero.
print('Verdadero mas Falso da: '+ str(valorOsi))

valorOsi = False or False# En este caso ambas son falsas.
print('Falso mas Falso da: '+ str(valorOsi))

nombre = 'Alberto'
valorOsi = nombre == 'salir' or nombre == 'terminar' or nombre == 'exit'
#aqui sera falso porque en ninguna  declaracion esta mi nombre
print('La respuesta es: ' + str(valorOsi))

# usando una lista seria asi
valorOsi = nombre[0:7] == 'Alberto'
print('El valor de mi nombre es: ' + str(valorOsi))
