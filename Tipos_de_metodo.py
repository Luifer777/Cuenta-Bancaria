class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def  pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} de huevos ")
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.poner_huevos(5)


Pajaro.mirar()
piolin = Pajaro('amarillo','canario')



