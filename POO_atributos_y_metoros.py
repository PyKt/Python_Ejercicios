import time
"""
Los atribustos son referencias a las variable internar y las funciones internas
"""
class Autos:# Auto es el metodo.
    pass
taller = Autos()
taller.color = "gris" #A partir del punto se esta ralizando la asignacion de los atributos
taller.puertas = 5
taller.brand = "Honda"
taller.model = "Fit"
taller.fabricacion = "Japon"
print('El color de la chonchi es:',taller.color)

class Autos:
    Rojo = True

objeto = Autos()
objeto.Rojo = False
print(objeto.Rojo)

class Honda:
    Rojo = False
    def __init__(self):
        print('Se construyo un auto')
    
    def fabricacion(self):
        self.Rojo = True
    def confirmacion_calidad(self):
        if (self.Rojo):
            print("Color correcto")
        else:
            print("Pintura equivocada")

marca = Honda()
marca.fabricacion()
marca.confirmacion_calidad()
print(marca.Rojo)

"""
Ahora vamos a usar los argumentos en las instanciaciones.
El uso de self lo que hace es hacer la referencia a la clase creada.
"""

class Fabricar_coche:

    def __init__(self,tiempo,marca,ruedas):
        self.tiempo = tiempo
        self.marca = marca
        self.ruedas = ruedas
        print("El coche de marca:",self.marca)

    def __del__(self):
        print("El coche:")

a1 = Fabricar_coche(5, "Honda", 4)

"""
Ahora aremos uso del metodo especial __str__ para convertir a cadena los datos
"""

class Fabricar_coche:
    def __init__(self, tiempo, marca, ruedas):
        self.tiempo = tiempo
        self.marca = marca
        self.ruedas = ruedas
        print("coche creado")

    def __del__(self):
        print("Finalizacion")
        
    def __str__(self):
        return "{} fue construido en el tiempo {} y cuenta con {} ruedas".format(self.marca, self.tiempo,self.ruedas)
    def __len__(self):
        return self.ruedas

a = Fabricar_coche(10, "Honda", 4)
print(a)
print(len(a)) ## Aqui llamamos la instaciacion __len__ dentro de la clase Fabricar_coche

"""
Seccion de Objetos embebidos
"""
class magnufactura:
    def __init__(self, brand,time,acount):
        self.brand = brand
        self.time = time
        self.acount = acount
        print("Seccion de Objetos embebidos")
        print("Aqui esta el elemento: {}".format(brand))

    def __str__(self):
        return "{}({})".format(self.nombre, self.tiempo)

class Listado:
    productos = []
    def __init__(self,productos=[]):
        self.productos = productos

    def matris_porductora(self, ob_de_magnufactura):
        self.matris_porductora.append(ob_de_magnufactura)

    def visualizar(self):
        for ob_de_magnufactura in self.matris_porductora:
            print(ob_de_magnufactura)

a = magnufactura("honda", 24, "cliente")

print('INGRESA EL DATO EN ESTA LISTA')
lista = str(input([]))

"""
Seccion de Objetos embebidos
"""

class Fabrica:
    def __init__(self, tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("Aqui esta el elemento: {}".format(nombre))

    def __str__(self):
        return "{}({})".format(self.nombre, self.tiempo)

class Listado:
    autos = []
    def __init__(self,autos=[]):
        self.autos = autos

    def fabricar(self, x):
        self.autos.append(x)

    def visualizar(self):
        for x in self.autos:
            print(x)

a = Fabrica(10, "Honda", 4)

l = Listado([a])
l.fabricar(Fabrica(15,"Civic",2))
l.visualizar()

"""
Simulacion de encapsulamiento en Python
"""

class encapsulamiento:
    __private_atri = print("Soy un atributo encapsulado por lo tanto no lo puedes ver desde fuera")
    def __metodo_privado(self):
        print("Soy un metodo privado por lo tando no me puedes ver fuera de la clase")

    def atributo_public(self):#Encontes para poder acceder a ellas se crean los atibutos publicos
        return self.__private_atri

    def metodo_public(self):
        return self.__metodo_privado()#Los metodos siempre se le debe colocar los entre parentesis()

oop = encapsulamiento()
oop.metodo_public()
oop.atributo_public()

#Las herencias en python, es lo que entrega una superclase a una clase hija o subclase
class Fabrica:# Esta es la super clase.
    def __init__(self,marca,nombre,precio,descripcion,ruedas,distribuidor=None):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.ruedas = ruedas
        self.distribuidor = distribuidor
    def __str__(self):
        return """
            MARCA\t{}
            NOMBRE\t{}
            PRECIO\t{}
            DESCRIPCION\t{}
            RUEDAS\t{}
            DISTRI\t{}""".format(self.marca,self.nombre,self.precio,self.descripcion,self.ruedas,self.distribuidor)

class Auto(Fabrica):
    pass
z = Auto('Honda','Fit',530000, 'Modelo 2014', 4, 'Hatch')
print(z)
class Deportivo(Fabrica):#Aqui Heredo los componentes de la clase padre y utilizo para crear un nuevo coche
    ruedas=""
    distribuidor = ""
    
    def __str__(self):
        return """
            MARCA\t{}
            NOMBRE\t{}
            PRECIO\t{}
            DESCRIPCION\t{}
            RUEDAS\t{}""".format(self.marca,self.nombre,self.precio,self.descripcion,self.ruedas)

coupe = Deportivo('AUDI','TT',2000000,'Rojo Convertible','Auto Premion')
coupe.ruedas = 4
print(coupe)
"""Proxima clase"""
