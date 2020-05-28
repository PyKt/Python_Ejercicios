

class Coche:
    marca = "mercedes"
    velocidad = 200
    modelo = "Serie 5"

    def __init__(self, marca, velocidad, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_velocidad(self):
        return self.velocidad


result = Coche(None, None, None)

result.set_marca("Honda")
result.set_modelo("Fit")
result.set_velocidad(200)

print(f"Mi chonchi es una {result.get_marca()}, modelo {result.get_modelo()} y vuela a {result.get_velocidad()}Kh")
"""
Getter para recuperar los datos
Setter para cambiar los datos.
"""
