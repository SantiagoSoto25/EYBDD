from queue import PriorityQueue
from typing import Tuple

class Documento:
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo

    def __lt__(self, other):
        return False

def imprimir_cola(cola: PriorityQueue[Tuple[int, Documento]]):
    print("\nDocumentos en la cola de impresión:")
    while not cola.empty():
        documento = cola.get()
        print(f"Documento: {documento[1].nombre} (Tipo: {documento[1].tipo})")

cola_impresion: PriorityQueue[Tuple[int, Documento]] = PriorityQueue()

cola_impresion.put((1, Documento("Doc1 (Empleado)", "Empleado")))
cola_impresion.put((1, Documento("Doc2 (Empleado)", "Empleado")))
cola_impresion.put((1, Documento("Doc3 (Empleado)", "Empleado")))

primer_documento = cola_impresion.get()
print(f"Documento impreso: {primer_documento[1].nombre}")

cola_impresion.put((2, Documento("Doc4 (TI)", "TI")))
cola_impresion.put((2, Documento("Doc5 (TI)", "TI")))

cola_impresion.put((3, Documento("Doc6 (Gerente)", "Gerente")))

segundo_documento = cola_impresion.get()
tercer_documento = cola_impresion.get()
print(f"Segundo documento impreso: {segundo_documento[1].nombre}")
print(f"Tercer documento impreso: {tercer_documento[1].nombre}")

cola_impresion.put((1, Documento("Doc7 (Empleado)", "Empleado")))
cola_impresion.put((1, Documento("Doc8 (Empleado)", "Empleado")))
cola_impresion.put((3, Documento("Doc9 (Gerente)", "Gerente")))

imprimir_cola(cola_impresion)
