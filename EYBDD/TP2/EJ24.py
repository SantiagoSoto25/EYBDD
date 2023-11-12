class Personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

pila_personajes = Pila()
pila_personajes.apilar(Personaje('Iron Man', 10))
pila_personajes.apilar(Personaje('Thor', 8))
pila_personajes.apilar(Personaje('Black Widow', 7))
pila_personajes.apilar(Personaje('Rocket Raccoon', 7))
pila_personajes.apilar(Personaje('Doctor Strange', 7))
pila_personajes.apilar(Personaje('Groot', 6))

posicion = 1
while not pila_personajes.esta_vacia():
    personaje = pila_personajes.desapilar()
    if personaje.nombre == 'Rocket Raccoon' or personaje.nombre == 'Groot':
        print(f'{personaje.nombre} está en la posición {posicion}')
        break
    posicion += 1

for personaje in pila_personajes.items:
    if personaje.peliculas > 5:
        print(f'{personaje.nombre} aparece en {personaje.peliculas} películas')

for personaje in pila_personajes.items:
    if personaje.nombre == 'Black Widow':
        print(f'{personaje.nombre} aparece en {personaje.peliculas} películas')

for personaje in pila_personajes.items:
    if personaje.nombre.startswith(('C', 'D', 'G')):
        print(personaje.nombre)