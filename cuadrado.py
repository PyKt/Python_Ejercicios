from figuraGeometrica import FiguraGeometrica
from color import PaletadeColores


class VolcadoDatos(FiguraGeometrica, ):

    def __init__(self, lado,ancho, color):
        self.color = color
        self.lado = lado
        self.ancho = ancho
        
    def areaCuadrado(self):
        return self.lado * self.ancho

    def seleccionColor(self):
        return "El color es",self.color




