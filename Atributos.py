class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.especie = especie
        self.color = color

mi_pajaro = Pajaro('negro', 'Tucan')

palabra = 'hola'

print(mi_pajaro.especie)
print(f"El color de mi pajaro es {mi_pajaro.color} y su especia es {mi_pajaro.especie}")

print(Pajaro.alas)

