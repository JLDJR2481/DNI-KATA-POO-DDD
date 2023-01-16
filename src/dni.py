from src.calculadoraLetra import CalculadoraLetra


class DNI(CalculadoraLetra):

    def __init__(self, numero):

        self.dni = ""
        self.letraDni = ""
        self.codigoDni = numero
        self.calculador = CalculadoraLetra()

    def checkFormatoDni(self):
        try:
            self.codigoDni = int(self.codigoDni)
        except:
            return False
        else:
            return True

    def checkLongitud(self):
        if len(self.codigoDni) != 8:
            return False
        else:
            return True

    def checkDni(self):
        if self.checkLongitud() and self.checkFormatoDni() == True:
            return True
        else:
            return False

    def calcularLetra(self):
        if self.checkDni() == True:
            posicion = self.calculador.calcularPosicion(self.codigoDni)
            try:
                self.letraDni = self.calculador.calcularLetra(posicion)
                return True
            except:
                return False
        else:
            return False

    def acoplarLetraDni(self):
        if self.calcularLetra() == True:
            self.dni = str(self.codigoDni) + self.letraDni
            return self.dni

        else:
            return 'Error, no es posible calcular la letra'
