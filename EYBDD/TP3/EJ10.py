from collections import deque
from typing import Deque

class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

def eliminar_notificaciones_facebook(cola_notificaciones):
    cola_filtrada = deque([noti for noti in cola_notificaciones if noti.aplicacion != 'Facebook'])
    cola_notificaciones.clear()
    cola_notificaciones.extend(cola_filtrada)

def mostrar_notificaciones_twitter_python(cola_notificaciones):
    notificaciones_twitter_python = deque()
    while cola_notificaciones:
        notificacion = cola_notificaciones.popleft()
        if notificacion.aplicacion == 'Twitter' and 'Python' in notificacion.mensaje:
            notificaciones_twitter_python.append(notificacion)
            print(f"Hora: {notificacion.hora}, Aplicación: {notificacion.aplicacion}, Mensaje: {notificacion.mensaje}")
    cola_notificaciones.extendleft(reversed(notificaciones_twitter_python))

def contar_notificaciones_temporales(cola_notificaciones, pila_temporal):
    contador = 0
    while cola_notificaciones:
        notificacion = cola_notificaciones.popleft()
        if '11:43' <= notificacion.hora <= '15:57':
            pila_temporal.append(notificacion)
            contador += 1
    return contador

cola_notificaciones = deque([
    Notificacion('11:30', 'Twitter', 'Mensaje con Python'),
    Notificacion('12:00', 'Facebook', 'Mensaje de Facebook'),
    Notificacion('14:00', 'Twitter', 'Otro mensaje'),
    Notificacion('15:50', 'Twitter', 'Mensaje sin Python')
])

pila_temporal: Deque[Notificacion] = deque()

print("Notificaciones antes:")
for noti in cola_notificaciones:
    print(f"Hora: {noti.hora}, Aplicación: {noti.aplicacion}, Mensaje: {noti.mensaje}")

eliminar_notificaciones_facebook(cola_notificaciones)
print("\nNotificaciones después de eliminar Facebook:")
for noti in cola_notificaciones:
    print(f"Hora: {noti.hora}, Aplicación: {noti.aplicacion}, Mensaje: {noti.mensaje}")

print("\nNotificaciones de Twitter con 'Python':")
mostrar_notificaciones_twitter_python(cola_notificaciones)

num_notificaciones_temporales = contar_notificaciones_temporales(cola_notificaciones, pila_temporal)
print(f"\nNúmero de notificaciones temporales entre 11:43 y 15:57: {num_notificaciones_temporales}")
