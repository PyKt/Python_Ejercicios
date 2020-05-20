print("Elije la opcion")

while True:
    print("""Elija la opcion correcta
    elije el numero de la opcion
    1 - Quiero que me saludes.
    2 - Deseo la tabla de multiplicar.
    3 - Salir del programa""")
    
    opcion = int(input())

    if opcion == 1:
        print("Hola usuario")
    elif opcion == 2:
        numero1 = float(input("Introduce el valor a multiplicar: "))
        numero2 = float(input("Introduce el otro valor a multiplicar: "))
        print("El resultado es:", numero1*numero2, )
    elif opcion == 3:
        print("Saliendo del programa")
        exit("saliendo...")

    else:
        raise ValueError ("Rango incorrecto")
    