import string
from io import open
import modulocoche

class Automovil:
    color = "gris"
    tipo = "hatchback"
    modelo = "fit"
    marca = "Honda"
    puertas = 5
    cilindraje = 1.5
    salida = 2014

    def __init__(self, color,tipo,modelo,marca,salida,puertas,cilindraje):

        self.salida = salida
        self.cilindraje = cilindraje
        self.puertas = puertas
        self.color = color
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def set_salida(self, salida):
        self.salida = salida

    def set_modelo(self,modelo):
        self.modelo = modelo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_color(self,color):
        self.color = color

    def set_puertas(self,puertas):
        self.puertas = puertas

    def set_cilindraje(self,cilindraje):
        self.cilindraje = cilindraje
    
    def set_marca(self, marca):
        self.marca = marca
    
    def get_salida(self):
        return self.salida
    
    def get_modelo(self):
        return self.modelo

    def get_tipo(self):
        return self.tipo

    def get_color(self):
        return self.color

    def get_puertas(self):
        return self.puertas

    def get_cilindraje(self):
        return self.cilindraje

    def get_marca(self):
        return self.marca
    
    def get_info(self):
        return print(f"""El vehiculo resultante es marca {self.marca} y cuenta con estas caracteristcas:
        TIPO\t {self.tipo} 
        FECHA\t {self.salida}
        COLOR\t {self.color}""")

produccion = Automovil("Gris","Hatchback", "Fit", "Honda",2015,5,4 )

