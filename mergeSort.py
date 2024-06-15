from datos_test import *

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

# Ordenar equipos dentro de cada sede por rendimiento usando merge sort
for sede in Sedes:
    for equipo in sede.equipos:
        equipo_ordenado = []
        raiz_equipo = None
        for jugador in equipo.jugadores:
            clave = (jugador.rendimiento, -jugador.edad)
            raiz_equipo = insertar(raiz_equipo, clave, Jugadores.index(jugador))
        recorrido_inorden(raiz_equipo, equipo_ordenado)
        equipo.jugadores = [Jugadores[i] for i in equipo_ordenado]

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
    return [jugadores_ordenados[i] + 1 for i in range(len(jugadores_ordenados))]

def equipoMayorRendimiento():
    mejor_rendimiento = max((sum(jugador.rendimiento for jugador in equipo.jugadores) / len(equipo.jugadores), equipo.deporte, sede.ciudad)
                            for sede in Sedes for equipo in sede.equipos)
    return mejor_rendimiento[1] + " Sede " + mejor_rendimiento[2]

def equipoMenorRendimiento():
    peor_rendimiento = min((sum(jugador.rendimiento for jugador in equipo.jugadores) / len(equipo.jugadores), equipo.deporte, sede.ciudad)
                           for sede in Sedes for equipo in sede.equipos)
    return peor_rendimiento[1] + " Sede " + peor_rendimiento[2]

def jugadorMayorRendimiento():
    jugador_id = jugadores_ordenados[-1]
    jugador = Jugadores[jugador_id]
    return (jugador_id + 1, jugador.nombre, jugador.rendimiento)

def jugadorMenorRendimiento():
    jugador_id = jugadores_ordenados[0]
    jugador = Jugadores[jugador_id]
    return (jugador_id + 1, jugador.nombre, jugador.rendimiento)

def jugadorMasJoven():
    edades = [(jugador.edad, jugador_id) for jugador_id, jugador in enumerate(Jugadores)]
    mergeSort(edades, 0, len(edades) - 1)
    jugador_id = edades[0][1]
    jugador = Jugadores[jugador_id]
    return (jugador_id + 1, jugador.nombre, jugador.edad)

def jugadorMasVeterano():
    edades = [(jugador.edad, jugador_id) for jugador_id, jugador in enumerate(Jugadores)]
    mergeSort(edades, 0, len(edades) - 1)
    jugador_id = edades[-1][1]
    jugador = Jugadores[jugador_id]
    return (jugador_id + 1, jugador.nombre, jugador.edad)

def promedioEdadJugador():
    edades = [jugador.edad for jugador in Jugadores]
    return sum(edades) / len(edades) if edades else 0

def promedioRendimientoJugador():
    rendimientos = [jugador.rendimiento for jugador in Jugadores]
    return sum(rendimientos) / len(rendimientos) if rendimientos else 0

# Imprimir resultados
for rendimiento_promedio, _, sede in rendimiento_sedes:
    print("Sede " + sede.ciudad + ", Rendimiento: " + str(rendimiento_promedio))
    for equipo in sede.equipos:
        rendimiento_equipo = sum(jugador.rendimiento for jugador in equipo.jugadores) / len(equipo.jugadores)
        print(equipo.deporte + ", Rendimiento: " + str(rendimiento_equipo))
        print("{" + ", ".join(str(Jugadores.index(jugador) + 1) for jugador in equipo.jugadores) + "}")

print("\nRanking de Jugadores:")
print("{" + ", ".join(str(id_jugador + 1) for id_jugador in rankingJugador()) + "}")

print("\nEquipo con Mayor Rendimiento:")
print(equipoMayorRendimiento())

print("\nEquipo con Menor Rendimiento:")
print(equipoMenorRendimiento())

print("\nJugador con Mayor Rendimiento:")
jug_may_rend = jugadorMayorRendimiento()
print("{" + str(jug_may_rend[0]) + " , " + jug_may_rend[1] + " , " + str(jug_may_rend[2]) + "}")

print("\nJugador con Menor Rendimiento:")
jug_men_rend = jugadorMenorRendimiento()
print("{" + str(jug_men_rend[0]) + " , " + jug_men_rend[1] + " , " + str(jug_men_rend[2]) + "}")

print("\nJugador Más Joven:")
jug_mas_joven = jugadorMasJoven()
print("{" + str(jug_mas_joven[0]) + " , " + jug_mas_joven[1] + " , " + str(jug_mas_joven[2]) + "}")

print("\nJugador Más Veterano:")
jug_mas_veterano = jugadorMasVeterano()
print("{" + str(jug_mas_veterano[0]) + " , " + jug_mas_veterano[1] + " , " + str(jug_mas_veterano[2]) + "}")

print("\nPromedio de Edad de los Jugadores:")
print(promedioEdadJugador())

print("\nPromedio de Rendimiento de los Jugadores:")
print(promedioRendimientoJugador())
