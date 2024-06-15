from datos_test import Jugadores, Sedes

class ABB:
    def __init__(self, clave, id_jugador):
        self.izquierda = None
        self.derecha = None
        self.val = clave
        self.id_jugador = id_jugador

def insertar(raiz, clave, id_jugador):
    if raiz is None:
        return ABB(clave, id_jugador)
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
def rendimiento_promedio_equipo(equipo):
    rendimiento_total = sum(jugador.rendimiento for jugador in equipo.jugadores)
    return rendimiento_total / len(equipo.jugadores) if equipo.jugadores else 0

# Ordenar jugadores por rendimiento usando árbol binario de búsqueda
jugadores_ordenados = []
raiz = None

for id_jugador, jugador in enumerate(Jugadores):
    clave = (jugador.rendimiento, -jugador.edad)
    raiz = insertar(raiz, clave, id_jugador)

recorrido_inorden(raiz, jugadores_ordenados)

# Ordenar equipos dentro de cada sede por rendimiento
for sede in Sedes:
    for equipo in sede.equipos:
        equipo_ordenado = []
        raiz_equipo = None
        for jugador in equipo.jugadores:
            clave = (jugador.rendimiento, -jugador.edad)
            raiz_equipo = insertar(raiz_equipo, clave, jugador)
        recorrido_inorden(raiz_equipo, equipo_ordenado)
        equipo.jugadores = equipo_ordenado

# Ordenar las sedes por rendimiento promedio y luego por cantidad de jugadores
rendimiento_sedes = []
for sede in Sedes:
    rendimiento_total = 0
    total_jugadores = 0
    for equipo in sede.equipos:
        rendimiento_total += sum(jugador.rendimiento for jugador in equipo.jugadores)
        total_jugadores += len(equipo.jugadores)
    rendimiento_promedio = rendimiento_total / total_jugadores if total_jugadores else 0
    rendimiento_sedes.append((rendimiento_promedio, -total_jugadores, sede))

mergeSort(rendimiento_sedes, 0, len(rendimiento_sedes) - 1)

# Funciones para obtener datos específicos
def rankingJugador():
    return [Jugadores[i].nombre for i in jugadores_ordenados]

def equipoMayorRendimiento():
    mejor_rendimiento = rendimiento_sedes[-1]
    return mejor_rendimiento[2].ciudad

def equipoMenorRendimiento():
    peor_rendimiento = rendimiento_sedes[0]
    return peor_rendimiento[2].ciudad

def jugadorMayorRendimiento():
    jugador_id = jugadores_ordenados[-1]
    jugador = Jugadores[jugador_id]
    return jugador_id, jugador.nombre, jugador.rendimiento

def jugadorMenorRendimiento():
    jugador_id = jugadores_ordenados[0]
    jugador = Jugadores[jugador_id]
    return jugador_id, jugador.nombre, jugador.rendimiento

def jugadorMasJoven():
    edades = [(jugador.edad, jugador_id) for jugador_id, jugador in enumerate(Jugadores)]
    mergeSort(edades, 0, len(edades) - 1)
    jugador_id = edades[0][1]
    jugador = Jugadores[jugador_id]
    return jugador_id, jugador.nombre, jugador.edad

def jugadorMasVeterano():
    edades = [(jugador.edad, jugador_id) for jugador_id, jugador in enumerate(Jugadores)]
    mergeSort(edades, 0, len(edades) - 1)
    jugador_id = edades[-1][1]
    jugador = Jugadores[jugador_id]
    return jugador_id, jugador.nombre, jugador.edad

def promedioEdadJugador():
    edades = [jugador.edad for jugador in Jugadores]
    return sum(edades) / len(edades) if edades else 0

def promedioRendimientoJugador():
    rendimientos = [jugador.rendimiento for jugador in Jugadores]
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
