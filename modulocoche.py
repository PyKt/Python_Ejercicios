class Coche:
    velocidad = 180
    marca = ""
    modelo = ""
    def __init__(self,marca,velocidad,modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def set_Velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_Modelo(self,modelo):
        self.modelo = modelo

    def set_Marca(self,marca):
        self.marca = marca
 
    ##Get asignacion:

    def get_Velocidad(self):
        self.velocidad = velocidad

    def get_Modelo(self,modelo):
        self.modelo = modelo

    def get_Marca(self,marca):
        self.marca = marca

juego = Coche("Honda",180,"Fit")
juego.set_Marca("Honda")




"""
Getter para recuperar los datos
Setter para cambiar los datos.
"""