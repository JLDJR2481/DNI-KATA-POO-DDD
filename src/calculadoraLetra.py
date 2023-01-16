class CalculadoraLetra:

    def __init__(self):
        self.tablaLetras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
                            'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

        self.longitud = len(self.tablaLetras)

    def calcularPosicion(self, numero):

        posicion = numero % self.longitud
        return posicion

    def calcularLetra(self, posicion):

        letra = self.tablaLetras[posicion]
        return letra
