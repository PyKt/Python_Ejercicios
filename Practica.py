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
base = input('Introduce la base imponible de la factura: ')

print(aplica_iva(base, iva))

def aplica_iva(base, iva = 21):
    base = base * iva   
    return base 