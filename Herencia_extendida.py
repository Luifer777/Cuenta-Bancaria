

# OTRO EJEMPLO DE HERENCIA

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja")
    def hablar(self):
        print("que tal")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.reir()
mi_nieto.hablar()
print(Nieto.__mro__)