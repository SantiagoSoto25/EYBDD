class Jedi:
    def __init__(self, nombre, especie, anio_nacimiento, color_sable, ranking, maestros):
        self.nombre = nombre
        self.especie = especie
        self.anio_nacimiento = anio_nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestros = maestros

def crear_arboles(jedis):
    arbol_nombre = {}
    arbol_ranking = {}
    arbol_especie = {}

    for jedi in jedis:
        arbol_nombre[jedi.nombre] = jedi

        if jedi.ranking not in arbol_ranking:
            arbol_ranking[jedi.ranking] = []
        arbol_ranking[jedi.ranking].append(jedi)

        if jedi.especie not in arbol_especie:
            arbol_especie[jedi.especie] = []
        arbol_especie[jedi.especie].append(jedi)

    return arbol_nombre, arbol_ranking, arbol_especie

def barrido_inorden(arbol):
    for key in sorted(arbol.keys()):
        if isinstance(arbol[key], list):
            for jedi in arbol[key]:
                print(jedi.nombre, jedi.ranking)
        else:
            print(arbol[key].nombre, arbol[key].ranking)

def barrido_por_nivel(arbol):
    for key in sorted(arbol.keys()):
        print(key)
        for jedi in arbol[key]:
            print("  ", jedi.nombre)

def mostrar_info(jedis, nombres):
    for nombre in nombres:
        jedi = jedis.get(nombre)
        if jedi:
            print(f"Nombre: {jedi.nombre}, Especie: {jedi.especie}, Año de nacimiento: {jedi.anio_nacimiento}, "
                  f"Color de sable: {jedi.color_sable}, Ranking: {jedi.ranking}, Maestros: {jedi.maestros}")
        else:
            print(f"No se encontró información para {nombre}")

def listar_jedi_color_verde(jedis):
    jedi_color_verde = [jedi.nombre for jedi in jedis if jedi.color_sable.lower() == 'verde']
    print("Jedi con sable de luz verde:", jedi_color_verde)

def listar_jedi_con_maestros(jedis):
    maestros_en_archivo = set(jedi.nombre for jedi in jedis)
    jedi_con_maestros = [jedi.nombre for jedi in jedis if any(maestro in maestros_en_archivo for maestro in jedi.maestros)]
    print("Jedi con maestros en el archivo:", jedi_con_maestros)

def mostrar_jedi_por_especie(jedis, especies):
    jedi_por_especie = [jedi for jedi in jedis if jedi.especie in especies]
    for jedi in jedi_por_especie:
        print(f"Nombre: {jedi.nombre}, Especie: {jedi.especie}")

def listar_jedi_letra_a_y_guion(jedis):
    jedi_letra_a_o_guion = [jedi.nombre for jedi in jedis if jedi.nombre.lower().startswith('a') or '-' in jedi.nombre]
    print("Jedi que comienzan con A o contienen un '-':", jedi_letra_a_o_guion)

jedi1 = Jedi("Yoda", "Desconocida", 896, "Verde", "Jedi Master", ["Desconocido"])
jedi2 = Jedi("Luke-Skywalker", "Humano", 19, "Azul", "Jedi Knight", ["Yoda", "Obi-Wan Kenobi"])
jedi3 = Jedi("Darth-Vader", "Humano", 300, "Rojo", "Padawan", ["yoda"])

jedis = [jedi1, jedi2, jedi3]
arbol_nombre, arbol_ranking, arbol_especie = crear_arboles(jedis)

print("Barrido inorden por nombre:")
barrido_inorden(arbol_nombre)

print("\nBarrido inorden por ranking:")
barrido_inorden(arbol_ranking)

print("\nBarrido por nivel por ranking:")
barrido_por_nivel(arbol_ranking)

print("\nBarrido por nivel por especie:")
barrido_por_nivel(arbol_especie)

print("\nMostrar información de Yoda y Luke-Skywalker:")
mostrar_info({jedi.nombre: jedi for jedi in jedis}, ["Yoda", "Luke-Skywalker"])

listar_jedi_color_verde(jedis)

listar_jedi_con_maestros(jedis)

mostrar_jedi_por_especie(jedis, ["Togruta", "Cerean"])

listar_jedi_letra_a_y_guion(jedis)
