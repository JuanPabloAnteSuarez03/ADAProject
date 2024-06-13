from datos import Jugadores, Sedes

class Jugador:
    def __init__(self, identificador, nombre, edad, rendimiento):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []  # Jugadores

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def rendimiento_promedio(self):
        total_rendimiento = sum(jugador.rendimiento for jugador in self.jugadores)
        return total_rendimiento / len(self.jugadores) if self.jugadores else 0

class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []  # Equipos

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def rendimiento_promedio(self):
        total_rendimiento = sum(equipo.rendimiento_promedio() for equipo in self.equipos)
        return total_rendimiento / len(self.equipos) if self.equipos else 0


# HeapSort
def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def ordenar_equipos(sede):
    equipos_con_rendimiento = [(equipo.rendimiento_promedio(), -len(equipo.jugadores), equipo) for equipo in sede.equipos]
    equipos_con_rendimiento = heapsort(equipos_con_rendimiento)
    sede.equipos = [equipo for _, _, equipo in equipos_con_rendimiento]

def ordenar_sedes(sedes):
    sedes_con_rendimiento = [(sede.rendimiento_promedio(), -sum(len(equipo.jugadores) for equipo in sede.equipos), sede) for sede in sedes]
    sedes_con_rendimiento = heapsort(sedes_con_rendimiento)
    return [sede for _, _, sede in sedes_con_rendimiento]

def generar_informe_jugadores_ordenados(sedes):
    jugadores = []
    for sede in sedes:
        for equipo in sede.equipos:
            jugadores.extend(equipo.jugadores)
    jugadores.sort(key=lambda jugador: jugador.rendimiento, reverse=True)
    informe = []
    for jugador in jugadores:
        informe.append(f"{jugador.identificador} - {jugador.nombre}, Edad: {jugador.edad}, Rendimiento: {jugador.rendimiento}")
    return "\n".join(informe)

def generar_informe_equipos_sedes(sedes):
    informe = []
    for sede in sedes:
        informe.append(f"Sede: {sede.nombre}")
        ordenar_equipos(sede)
        for equipo in sede.equipos:
            informe.append(f"  Equipo: {equipo.nombre}, Rendimiento Promedio: {equipo.rendimiento_promedio()}")
            jugadores_ordenados = sorted(equipo.jugadores, key=lambda jugador: jugador.rendimiento)
            for jugador in jugadores_ordenados:
                informe.append(f"    Jugador: {jugador.identificador} - {jugador.nombre}, Edad: {jugador.edad}, Rendimiento: {jugador.rendimiento}")
    return "\n".join(informe)

def equipoMayorRendimiento(sedes):
    mayor_equipo = None
    mayor_rendimiento = -1
    sede_nombre = ""
    for sede in sedes:
        for equipo in sede.equipos:
            rendimiento = equipo.rendimiento_promedio()
            if rendimiento > mayor_rendimiento:
                mayor_rendimiento = rendimiento
                mayor_equipo = equipo
                sede_nombre = sede.nombre
    return f"{mayor_equipo.nombre} de la sede {sede_nombre}" if mayor_equipo else None

def equipoMenorRendimiento(sedes):
    menor_equipo = None
    menor_rendimiento = float('inf')
    sede_nombre = ""
    for sede in sedes:
        for equipo in sede.equipos:
            rendimiento = equipo.rendimiento_promedio()
            if rendimiento < menor_rendimiento:
                menor_rendimiento = rendimiento
                menor_equipo = equipo
                sede_nombre = sede.nombre
    return f"{menor_equipo.nombre} de la sede {sede_nombre}" if menor_equipo else None

def jugadorMayorRendimiento(jugadores):
    mayor_jugador = max(jugadores.values(), key=lambda jugador: jugador.rendimiento)
    return (mayor_jugador.nombre, mayor_jugador.rendimiento)

def jugadorMenorRendimiento(jugadores):
    menor_jugador = min(jugadores.values(), key=lambda jugador: jugador.rendimiento)
    return (menor_jugador.nombre, menor_jugador.rendimiento)

def jugadorMasJoven(jugadores):
    mas_joven = min(jugadores.values(), key=lambda jugador: jugador.edad)
    return (mas_joven.nombre, mas_joven.edad)

def jugadorMasVeterano(jugadores):
    mas_veterano = max(jugadores.values(), key=lambda jugador: jugador.edad)
    return (mas_veterano.nombre, mas_veterano.edad)

def promedioEdadJugadores(jugadores):
    edades = [jugador.edad for jugador in jugadores.values()]
    return sum(edades) / len(edades) if edades else 0

def promedioRendimientoJugadores(jugadores):
    rendimientos = [jugador.rendimiento for jugador in jugadores.values()]
    return round(sum(rendimientos) / len(rendimientos), 2) if rendimientos else 0


# Crear instancias de jugadores, equipos y sedes usando los datos definidos en datos.py
jugadores = {id: Jugador(id, data["Nombre"], data["Edad"], data["Rendimiento"]) for id, data in Jugadores.items()}
equipos_sedes = {}

for sede_id, sede_data in Sedes.items():
    sede = Sede(sede_data["Ciudad"])
    for deporte, jugadores_ids in sede_data["Equipos"].items():
        equipo = Equipo(deporte)
        for jugador_id in jugadores_ids:
            equipo.agregar_jugador(jugadores[jugador_id])
        sede.agregar_equipo(equipo)
    equipos_sedes[sede_id] = sede

# Ordenar las sedes y generar informes
sedes_ordenadas = ordenar_sedes(list(equipos_sedes.values()))
informe_jugadores = generar_informe_jugadores_ordenados(sedes_ordenadas)
informe_equipos_sedes = generar_informe_equipos_sedes(sedes_ordenadas)

print("Informe de Jugadores Ordenados por Rendimiento:")
print(informe_jugadores)
print("\nInforme de Equipos Ordenados por Sedes:")
print(informe_equipos_sedes)

print("\nEquipo con mayor rendimiento:")
print(equipoMayorRendimiento(sedes_ordenadas))

print("\nEquipo con menor rendimiento:")
print(equipoMenorRendimiento(sedes_ordenadas))

print("\nJugador con mayor rendimiento:")
print(jugadorMayorRendimiento(jugadores))

print("\nJugador con menor rendimiento:")
print(jugadorMenorRendimiento(jugadores))

print("\nJugador más joven:")
print(jugadorMasJoven(jugadores))

print("\nJugador más veterano:")
print(jugadorMasVeterano(jugadores))

print("\nPromedio de edad de los jugadores:")
print(promedioEdadJugadores(jugadores))

print("\nPromedio de rendimiento de los jugadores:")
print(promedioRendimientoJugadores(jugadores))