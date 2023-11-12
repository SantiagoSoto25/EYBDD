superheroes = {
    "Superman": {
        "año_aparicion": 1938,
        "casa_comic": "DC",
        "biografia": "Superman es un superhéroe que vuela y tiene superpoderes."
    },
    "Batman": {
        "año_aparicion": 1939,
        "casa_comic": "DC",
        "biografia": "Batman lucha contra el crimen en Gotham City."
    },
    "Spider-Man": {
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Spider-Man tiene habilidades arácnidas y un traje especial."
    },
    "Linterna-Verde": {
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Linterna verde se encuentra un anillo que le da poderes"
    },
    "Wolverine": {
        "año_aparicion": 1974,
        "casa_comic": "DC",
        "biografia": "Es un mutante que posee sentidos afinados de los animales"
    },
    "Dr. Strange": {
        "año_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Un increible mago que tiene un gran abanico de poderes"
    },
    "Capitana Marvel": {
        "año_aparicion": 1968,
        "casa_comic": "Marvel",
        "biografia": "Una chica con poderes cosmicos"
    },
    "Mujer Maravilla": {
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Princesa guerrera de las Amazonas con una gran fuerza y una gran armadura"
    },
    "Star-Lord": {
        "año_aparicion": 1976,
        "casa_comic": "Marvel",
        "biografia": "Lleva un traje que le otorga fuerza y durabilidad aumentadas, además de la habilidad de viajar a través del espacio"
    },
    "Flash": {
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "posee una rapidez sobrehumana, la cual incluye la habilidad de correr a gran velocidad y reflejos sobrehumanos"
    }
}

del superheroes["Linterna-Verde"]

print(superheroes["Wolverine"]["año_aparicion"])

superheroes["Dr. Strange"]["casa_comic"] = "Marvel"

nombres_con_traje_o_armadura = [nombre for nombre, datos in superheroes.items() if "biografia" in datos and ("traje" in str(datos["biografia"]) or "armadura" in str(datos["biografia"]))]
for nombre in nombres_con_traje_o_armadura:
    print(nombre)

anteriores_1963 = [(nombre, datos["casa_comic"]) for nombre, datos in superheroes.items() if isinstance(datos["año_aparicion"], int) and datos["año_aparicion"] < 1963]
print(anteriores_1963)

print(anteriores_1963)

casa_capitana_marvel = superheroes["Capitana Marvel"]["casa_comic"]
casa_mujer_maravilla = superheroes["Mujer Maravilla"]["casa_comic"]
print(f"Capitana Marvel pertenece a la casa {casa_capitana_marvel}")
print(f"Mujer Maravilla pertenece a la casa {casa_mujer_maravilla}")

print(f"La informacion de Flash es la siguiente:", superheroes["Flash"])
print(f"La informacion de Star-Lord es la siguiente:", superheroes["Star-Lord"])

superheroes_b = [nombre for nombre in superheroes.keys() if nombre.startswith("B")]
superheroes_m = [nombre for nombre in superheroes.keys() if nombre.startswith("M")]
superheroes_s = [nombre for nombre in superheroes.keys() if nombre.startswith("S")]
print("Superhéroes que comienzan con B:", superheroes_b)
print("Superhéroes que comienzan con M:", superheroes_m)
print("Superhéroes que comienzan con S:", superheroes_s)

num_dc = sum(1 for datos in superheroes.values() if datos["casa_comic"] == "DC")
num_marvel = sum(1 for datos in superheroes.values() if datos["casa_comic"] == "Marvel")
print(f"Superhéroes de DC: {num_dc}")
print(f"Superhéroes de Marvel: {num_marvel}")
