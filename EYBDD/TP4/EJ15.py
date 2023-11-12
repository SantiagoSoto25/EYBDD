class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, pokemons):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = pokemons

entrenadores = [
    #Torneos ganados, Batallas perdidas, Batallas ganadas, Nivel Pokemon
    Entrenador("Ash", 5, 10, 15, [Pokemon("Voltron", 30, "Eléctrico", None)]),
    Entrenador("Misty", 3, 5, 8, [Pokemon("Starmie", 35, "Agua", "Psíquico")]),
    Entrenador("Santiago", 4, 2, 8, [Pokemon("Flareon", 45, "Fuego", None)]),
]

nuevo_pokemon1 = Pokemon("Vaporeon", 45, "Agua", None)
nuevo_pokemon2 = Pokemon("Terrakion", 45, "Roca", None)

santiago = entrenadores[2]

santiago.pokemons.append(nuevo_pokemon1)
santiago.pokemons.append(nuevo_pokemon2)

def cantidad_de_pokemons(entrenador):
    return len(entrenador.pokemons)

def entrenadores_ganadores(entrenadores):
    return [entrenador for entrenador in entrenadores if entrenador.torneos_ganados > 3]

def pokemon_mas_fuerte(entrenadores):
    entrenador_mas_ganador = max(entrenadores, key=lambda x: x.torneos_ganados)
    pokemon_mas_fuerte = max(entrenador_mas_ganador.pokemons, key=lambda x: x.nivel)
    return pokemon_mas_fuerte

def datos_entrenador(entrenador):
    print(f"Nombre: {entrenador.nombre}")
    print(f"Torneos ganados: {entrenador.torneos_ganados}")
    print(f"Batallas perdidas: {entrenador.batallas_perdidas}")
    print(f"Batallas ganadas: {entrenador.batallas_ganadas}")
    print("Pokémons:")
    for pokemon in entrenador.pokemons:
        print(f"Nombre: {pokemon.nombre}, Nivel: {pokemon.nivel}, Tipo: {pokemon.tipo}, Subtipo: {pokemon.subtipo}")

def entrenadores_con_porcentaje_alto(entrenadores):
    return [entrenador for entrenador in entrenadores if (entrenador.batallas_ganadas / (entrenador.batallas_ganadas + entrenador.batallas_perdidas)) > 0.79]

def entrenadores_con_tipos_especificos(entrenadores):
    return [entrenador for entrenador in entrenadores if any(pokemon.tipo == "Fuego" and (pokemon.subtipo == "Planta" or pokemon.subtipo == "Agua/Volador") for pokemon in entrenador.pokemons)]

def promedio_nivel_pokemons(entrenador):
    if not entrenador.pokemons:
        return 0
    return sum(pokemon.nivel for pokemon in entrenador.pokemons) / len(entrenador.pokemons)

def entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    return [entrenador for entrenador in entrenadores if any(pokemon.nombre == nombre_pokemon for pokemon in entrenador.pokemons)]

def entrenadores_con_pokemons_repetidos(entrenadores):
    nombres_pokemon = set()
    entrenadores_con_repetidos = []
    for entrenador in entrenadores:
        for pokemon in entrenador.pokemons:
            if pokemon.nombre in nombres_pokemon:
                entrenadores_con_repetidos.append(entrenador)
                break
            nombres_pokemon.add(pokemon.nombre)
    return entrenadores_con_repetidos

def entrenadores_con_ciertos_pokemons(entrenadores, nombres_pokemons):
    return [entrenador for entrenador in entrenadores if any(pokemon.nombre in nombres_pokemons for pokemon in entrenador.pokemons)]

def buscar_entrenador_y_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    for entrenador in entrenadores:
        if entrenador.nombre == nombre_entrenador:
            for pokemon in entrenador.pokemons:
                if pokemon.nombre == nombre_pokemon:
                    print(f"Entrenador: {entrenador.nombre}")
                    print(f"Pokémon: {pokemon.nombre}, Nivel: {pokemon.nivel}, Tipo: {pokemon.tipo}, Subtipo: {pokemon.subtipo}")
                    return
    print(f"No se encontró al entrenador {nombre_entrenador} o al Pokémon {nombre_pokemon}")

print("Cantidad de Pokémon de Santiago:", cantidad_de_pokemons(entrenadores[2]))

print("Entrenadores ganadores:", [entrenador.nombre for entrenador in entrenadores_ganadores(entrenadores)])

print("Pokemon más fuerte del entrenador con más torneos ganados:", pokemon_mas_fuerte(entrenadores).nombre)

print("Datos de Ash:")
datos_entrenador(entrenadores[0])

print("Entrenadores con porcentaje alto de batallas ganadas:", [entrenador.nombre for entrenador in entrenadores_con_porcentaje_alto(entrenadores)])

print("Entrenadores con tipos específicos:", [entrenador.nombre for entrenador in entrenadores_con_tipos_especificos(entrenadores)])

print("Promedio de nivel de los Pokémon de Ash:", promedio_nivel_pokemons(entrenadores[0]))

print("Entrenadores con Pikachu:", [entrenador.nombre for entrenador in entrenadores_con_pokemon(entrenadores, "Pikachu")])

print("Entrenadores con Pokémon repetidos:", [entrenador.nombre for entrenador in entrenadores_con_pokemons_repetidos(entrenadores)])

print("Entrenadores con ciertos Pokémon:", [entrenador.nombre for entrenador in entrenadores_con_ciertos_pokemons(entrenadores, ["Tyrantrum", "Terrakion", "Wingull"])])

nombre_entrenador_buscar = input("Ingresa el nombre del entrenador que deseas buscar: ")
nombre_pokemon_buscar = input("Ingresa el nombre del pokemon que deseas buscar: ")

buscar_entrenador_y_pokemon(entrenadores, nombre_entrenador_buscar, nombre_pokemon_buscar)
