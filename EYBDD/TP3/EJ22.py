from collections import deque

def procesar_cola(cola):
    for personaje in cola:
        if personaje[1] == 'Capitana Marvel':
            print(f'El nombre del personaje de Capitana Marvel es {personaje[0]}')
            break

    print('Superhéroes femeninos:')
    for personaje in cola:
        if personaje[2] == 'F':
            print(personaje[1])

    print('Superhéroes masculinos:')
    for personaje in cola:
        if personaje[2] == 'M':
            print(personaje[0])

    for personaje in cola:
        if personaje[0] == 'Scott Lang':
            print(f'El nombre del superhéroe de Scott Lang es {personaje[1]}')
            break

    print('Superhéroes o personajes cuyos nombres comienzan con la letra S:')
    for personaje in cola:
        if personaje[0][0] == 'S' or personaje[1][0] == 'S':
            print(personaje)

    for personaje in cola:
        if personaje[0] == 'Carol Danvers':
            print(f'Carol Danvers se encuentra en la cola y su nombre de superhéroe es {personaje[1]}')
            break
    else:
        print('Carol Danvers no se encuentra en la cola')

cola = deque([
    ('Tony Stark', 'Iron Man', 'M'),
    ('Steve Rogers', 'Capitán América', 'M'),
    ('Natasha Romanoff', 'Black Widow', 'F'),
    ('Carol Danvers', 'Capitana Marvel', 'F'),
    ('Scott Lang', 'Ant-Man', 'M')
])

procesar_cola(cola)