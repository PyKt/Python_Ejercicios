import subprocess

print("Hola y bienvenido a esta practica de siclo While")

c = str(input("Deseas continuar. y/n \n"))

if c =='y':
    subprocess.call(['clear'])
if c =="n":
     exit('Saliendo del miniprograma...')

dato = 'inicio'

while dato:
    print("""Evaluemos el sistema.
            1 - Comporbar si tenemos actualizaciones
            2 - Limpiar el cache del sistema.
            3 - Test de velocidad de Internet.
            0 - Salir del menu""")
    try:
        dato = int(input())#aqui reasigno el valor de dato
    except:
        subprocess.call(['clear'])
        print("Solo puedes seleccionar numeros. \nPreciones ENTER para continuar")
        input()

    if dato == 1:
        subprocess.call(['yay'])
        subprocess.call(['clear'])

    if dato == 2:    
        subprocess.call(['yay', '-Scc'])
        subprocess.call('clear')
   
    if dato == 3:
        subprocess.call(['speedtest-cli'])
    
    elif dato == 0:
        print('Saliendo del miniprograma...')
    
    else:
      print('Numeral equivocado')


contador = 1
muestra = str(0)
while contador <= 100:
    muestra = muestra + "," +str(contador)
    contador +=1

print(muestra)
numero = int(input())
tabla_multiplicar =1 
while tabla_multiplicar <= 10:
    print(f"{numero} x {tabla_multiplicar} = {numero*tabla_multiplicar}")
    tabla_multiplicar +=1