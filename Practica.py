class Honda:
    def segmento(self):
        tipo = "Hatchback"
    def pintura(self):
        color = "Gris"

class Toyota:
    def segmento(self):
        tipo = "Sedan"
    def pintura(self):
        color = "Rojo"

def poli(objecto):
    objecto.segmento()
    objecto.pintura()

nuevo_honda = Honda()
poli(objecto=nuevo_honda)
