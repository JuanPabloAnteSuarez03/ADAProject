# Datos importados de datos.py
from datos import *

class NodoAB:
    def __init__(self, clave, id_jugador):
        self.izquierda = None
        self.derecha = None
        self.val = clave
        self.id_jugador = id_jugador

def insertar(raiz, clave, id_jugador):
    if raiz is None:
        return NodoAB(clave, id_jugador)
    else:
        if raiz.val < clave:
            raiz.derecha = insertar(raiz.derecha, clave, id_jugador)
        else:
            raiz.izquierda = insertar(raiz.izquierda, clave, id_jugador)
    return raiz

def recorrido_inorden(raiz, jugadores_ordenados):
    if raiz:
        recorrido_inorden(raiz.izquierda, jugadores_ordenados)
        jugadores_ordenados.append(raiz.id_jugador)
        recorrido_inorden(raiz.derecha, jugadores_ordenados)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

# Función para obtener los rendimientos promedios de los equipos y sedes
def rendimiento_promedio_equipo(equipo, jugadores):
    rendimiento_total = sum(jugadores[id_jugador]["Rendimiento"] for id_jugador in equipo)
    return rendimiento_total / len(equipo) if equipo else 0

# Ordenar jugadores por rendimiento usando árbol binario de búsqueda
jugadores_ordenados = []
raiz = None

for id_jugador in Jugadores:
    info_jugador = Jugadores[id_jugador]
    clave = (info_jugador["Rendimiento"], -info_jugador["Edad"])
    raiz = insertar(raiz, clave, id_jugador)

recorrido_inorden(raiz, jugadores_ordenados)

# Ordenar equipos dentro de cada sede por rendimiento usando merge sort
for sede_id in Sedes:
    sede = Sedes[sede_id]
    for deporte in sede["Equipos"]:
        equipo = sede["Equipos"][deporte]
        arr = equipo[:]
        mergeSort(arr, 0, len(arr) - 1)
        sede["Equipos"][deporte] = arr

# Ordenar las sedes por rendimiento promedio y luego por cantidad de jugadores
rendimiento_sedes = []
for sede_id in Sedes:
    sede = Sedes[sede_id]
    rendimiento_total = 0
    total_jugadores = 0
    for deporte in sede["Equipos"]:
        equipo = sede["Equipos"][deporte]
        rendimiento_total += sum(Jugadores[id_jugador]["Rendimiento"] for id_jugador in equipo)
        total_jugadores += len(equipo)
    rendimiento_promedio = rendimiento_total / total_jugadores if total_jugadores else 0
    rendimiento_sedes.append((rendimiento_promedio, -total_jugadores, sede_id))

mergeSort(rendimiento_sedes, 0, len(rendimiento_sedes) - 1)

# Funciones actualizadas con Merge Sort

def rankingJugador():
    return jugadores_ordenados

def equipoMayorRendimiento():
    mejor_rendimiento = rendimiento_sedes[-1]
    sede_id = mejor_rendimiento[2]
    return Sedes[sede_id]["Ciudad"]

def equipoMenorRendimiento():
    peor_rendimiento = rendimiento_sedes[0]
    sede_id = peor_rendimiento[2]
    return Sedes[sede_id]["Ciudad"]

def jugadorMayorRendimiento():
    jugador_id = jugadores_ordenados[-1]
    jugador_info = Jugadores[jugador_id]
    return jugador_id, jugador_info["Nombre"], jugador_info["Rendimiento"]

def jugadorMenorRendimiento():
    jugador_id = jugadores_ordenados[0]
    jugador_info = Jugadores[jugador_id]
    return jugador_id, jugador_info["Nombre"], jugador_info["Rendimiento"]

def jugadorMasJoven():
    edades = [(Jugadores[jugador_id]["Edad"], jugador_id) for jugador_id in Jugadores]
    mergeSort(edades, 0, len(edades) - 1)
    jugador_id = edades[0][1]
    jugador_info = Jugadores[jugador_id]
    return jugador_id, jugador_info["Nombre"], jugador_info["Edad"]

def jugadorMasVeterano():
    edades = [(Jugadores[jugador_id]["Edad"], jugador_id) for jugador_id in Jugadores]
    mergeSort(edades, 0, len(edades) - 1)
    jugador_id = edades[-1][1]
    jugador_info = Jugadores[jugador_id]
    return jugador_id, jugador_info["Nombre"], jugador_info["Edad"]

def promedioEdadJugador():
    edades = [Jugadores[jugador_id]["Edad"] for jugador_id in Jugadores]
    return sum(edades) / len(edades) if edades else 0

def promedioRendimientoJugador():
    rendimientos = [Jugadores[jugador_id]["Rendimiento"] for jugador_id in Jugadores]
    return sum(rendimientos) / len(rendimientos) if rendimientos else 0

# Imprimir resultados
print("Ranking de Jugadores:")
print(rankingJugador())

print("\nEquipo con Mayor Rendimiento:")
print(equipoMayorRendimiento())

print("\nEquipo con Menor Rendimiento:")
print(equipoMenorRendimiento())

print("\nJugador con Mayor Rendimiento:")
print(jugadorMayorRendimiento())

print("\nJugador con Menor Rendimiento:")
print(jugadorMenorRendimiento())

print("\nJugador Más Joven:")
print(jugadorMasJoven())

print("\nJugador Más Veterano:")
print(jugadorMasVeterano())

print("\nPromedio de Edad de los Jugadores:")
print(promedioEdadJugador())

print("\nPromedio de Rendimiento de los Jugadores:")
print(promedioRendimientoJugador())