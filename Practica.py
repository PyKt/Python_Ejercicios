# Polimorfismos con funciones

class Honda:
    def segmento(self):
        print("Hatchback")
    def pintura(self):
        print("Gris")

class Toyota:
    def segmento(self):
        print("Sedan")
    def pintura(self):
        print("Rojo")

def poli(objecto):
    objecto.segmento()
    objecto.pintura()

nuevo_honda = Honda()
poli(nuevo_honda)

nuevo_toyota = Toyota()
poli(nuevo_toyota)

#Polimorfismo con metodos
