from TP5_arbolbinario import BinaryTree

arbol = BinaryTree()


lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'doctor strange', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': False},
    {'name': 'rhino', 'heroe': False},
    {'name': 'juggernaut', 'heroe': False},
    {'name': 'deadpool', 'heroe': True}
]

# Insert heroes and villains into the binary tree
for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])

# b
arbol.inorden_super_or_villano(False)
print()

# c
arbol.inorden_start_with('C')
print()

# d
print('Cantidad de superheroes:', arbol.contar_heroes())
print()

# e
search_term = input('Ingrese el término de búsqueda: ')
arbol.search_by_coincidence(search_term)

modify_name = input('Ingrese el nombre que desea modificar: ')
node_to_modify = arbol.search(modify_name)

if node_to_modify:
    is_hero = node_to_modify.other_values
    arbol.delete_node(modify_name)
    print('Modificar')
    new_name = input('Ingrese el nuevo nombre: ')
    arbol.insert_node(new_name, is_hero)
else:
    print('No se encontró el nombre.')

print()
arbol.inorden()

# f
#arbol.by_level()

# g
superheroes = BinaryTree()
villains = BinaryTree()

arbol.get_heroe_villano(superheroes, villains)
print()
print(f'Los héroes son {superheroes.contar_heroes()}')
print(f'Los villanos son {villains.contar_villanos()}')

print()
print('Superhéroes:')
superheroes.inorden()

print()
print('Villanos:')
villains.inorden()