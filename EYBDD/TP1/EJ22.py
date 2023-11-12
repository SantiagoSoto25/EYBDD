def usar_la_fuerza(mochila, contador=0):
    if len(mochila) == 0:
        print('No encontré un sable de luz en la mochila.')
        return
    objeto = mochila.pop(0)
    contador += 1
    if objeto == 'sable de luz':
        print('Encontré un sable de luz después de sacar', contador, 'objetos.')
        return
    else:
        print('Saqué', objeto, 'de la mochila.')
        usar_la_fuerza(mochila, contador)
mochila = ['una Esfera de la paz', 'unos Dados de Han Solo', 'una Aerolupa', 'un Mapa Estelar', 'sable de luz']
usar_la_fuerza(mochila)