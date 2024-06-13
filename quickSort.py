from datos import *
import statistics


def rankingJugador(Jugadores):
    rendimientos = [(Jugadores[j]["Rendimiento"], j) for j in Jugadores]
    rendimientos = quicksort(rendimientos)
    jugadoresOrdenados = [j for _, j in rendimientos]
    return jugadoresOrdenados

def equipoMayorRendimiento(Sedes, Jugadores, M):
    arr = ordenarSedes(Sedes, Jugadores, M)
    return arr[0][1][0][0] + " sede " + arr[0][0]

def equipoMenorRendimiento(Sedes, Jugadores, M):
    arr = ordenarSedes(Sedes, Jugadores, M)
    return arr[-1][-1][-1][0] + " sede " + arr[-1][0]

def jugadorMayorRendimiento(Jugadores):
    jugadoresOrdenados = rankingJugador(Jugadores)
    return (jugadoresOrdenados[-1], Jugadores[jugadoresOrdenados[-1]]["Nombre"], Jugadores[jugadoresOrdenados[-1]]["Rendimiento"])
    
def jugadorMenorRendimiento(Jugadores):
    jugadoresOrdenados = rankingJugador(Jugadores)
    return (jugadoresOrdenados[0], Jugadores[jugadoresOrdenados[0]]["Nombre"], Jugadores[jugadoresOrdenados[0]]["Rendimiento"])

def jugadorMasJoven(Jugadores):
    edades = [(Jugadores[j]["Edad"], j) for j in Jugadores]
    edades = quicksort(edades)
    jugadoresOrdenados = [j for _, j in edades]
    return (jugadoresOrdenados[0], Jugadores[jugadoresOrdenados[0]]["Nombre"], Jugadores[jugadoresOrdenados[0]]["Edad"])

def jugadormasVeterano(Jugadores):
    edades = [(Jugadores[j]["Edad"], j) for j in Jugadores]
    edades = quicksort(edades)
    jugadoresOrdenados = [j for _, j in edades]
    return (jugadoresOrdenados[-1], Jugadores[jugadoresOrdenados[-1]]["Nombre"], Jugadores[jugadoresOrdenados[-1]]["Edad"])

def promedioEdadJugador(Jugadores):
    edades = [Jugadores[j]["Edad"] for j in Jugadores]
    promedio = sum(edades) / len(edades)
    return promedio

def promedioRendimientoJugador(Jugadores):
    rendimientos = [Jugadores[j]["Rendimiento"] for j in Jugadores]
    promedio = sum(rendimientos) / len(rendimientos)
    return promedio

# Usaremos QuickSort como algoritmo de ordenamiento
def quicksort(arr):
    def particion(bajo, alto):
        pivot = arr[alto]
        i = bajo - 1
        
        for j in range(bajo, alto):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1

    def quicksort_recursive(bajo, alto):
        if bajo < alto:
            pi = particion(bajo, alto)
            quicksort_recursive(bajo, pi - 1)
            quicksort_recursive(pi + 1, alto)
    
    quicksort_recursive(0, len(arr) - 1)
    return arr

def ordenarJugadores(Sedes, Jugadores, M):
    for i in range(1, M+1):
        rendimientosFutbol = []
        rendimientosVolleyball = []
        listaFutbol = Sedes[i]["Equipos"]["Futbol"]
        listaVolleyball = Sedes[i]["Equipos"]["Volleyball"]
        
        for j in listaFutbol:
            rendimientosFutbol.append((Jugadores[j]["Rendimiento"], j))
        
        for h in listaVolleyball:
            rendimientosVolleyball.append((Jugadores[h]["Rendimiento"], h))
        
        rendimientosFutbol = quicksort(rendimientosFutbol)
        rendimientosVolleyball = quicksort(rendimientosVolleyball)
        
        Sedes[i]["Equipos"]["Futbol"] = [j for rendimiento, j in rendimientosFutbol]
        Sedes[i]["Equipos"]["Volleyball"] = [h for rendimiento, h in rendimientosVolleyball]
    
    return Sedes


def ordenarEquipos(Sedes, Jugadores, M):
    Sedes = ordenarJugadores(Sedes, Jugadores, M)
    
    sedes_ordenadas = []
    
    for i in range(1, M+1):
        sede = Sedes[i]
        equipos_rendimiento = []
        
        for equipo in sede["Equipos"]:
            rendimientos = [Jugadores[j]["Rendimiento"] for j in sede["Equipos"][equipo]]
            promedio_rendimiento = sum(rendimientos) / len(rendimientos)
            equipos_rendimiento.append((promedio_rendimiento, equipo, sede["Equipos"][equipo]))
        
        equipos_rendimiento = quicksort(equipos_rendimiento)
        equipos_rendimiento.reverse()  
        
        equipos_ordenados = [(equipo, jugadores) for _, equipo, jugadores in equipos_rendimiento]
        
        sedes_ordenadas.append((sede["Ciudad"], equipos_ordenados))
    
    return sedes_ordenadas


def ordenarSedes(Sedes, Jugadores, M):
    Sedes = ordenarJugadores(Sedes, Jugadores, M)
    
    sedes_ordenadas = []
    
    for i in range(1, M+1):
        sede = Sedes[i]
        equipos_rendimiento = []
        
        for equipo in sede["Equipos"]:
            rendimientos = [Jugadores[j]["Rendimiento"] for j in sede["Equipos"][equipo]]
            promedio_rendimiento = sum(rendimientos) / len(rendimientos)
            equipos_rendimiento.append((promedio_rendimiento, equipo, sede["Equipos"][equipo]))
        
        equipos_rendimiento = quicksort(equipos_rendimiento)
        equipos_rendimiento.reverse()  
        
        equipos_ordenados = [(equipo, jugadores) for _, equipo, jugadores in equipos_rendimiento]
        
        sedes_ordenadas.append((sede["Ciudad"], equipos_ordenados))
    
    sedes_ordenadas = quicksort(sedes_ordenadas)
    sedes_ordenadas.reverse()
    
    return sedes_ordenadas


print("\nOrdenar jugadores por rendimiento en cada sede:")
print(ordenarJugadores(Sedes, Jugadores, M))

print("\nOrdenar equipos por promedio de rendimiento en cada sede:")
print(ordenarEquipos(Sedes, Jugadores, M))

print("\nOrdenar sedes por promedio de rendimiento de los equipos:")
print(ordenarSedes(Sedes, Jugadores, M))

print("\nEquipo con mayor rendimiento:")
print(equipoMayorRendimiento(Sedes, Jugadores, M))

print("\nEquipo con menor rendimiento:")
print(equipoMenorRendimiento(Sedes, Jugadores, M))

print("\nJugador con mayor rendimiento:")
print(jugadorMayorRendimiento(Jugadores))

print("\nJugador con menor rendimiento:")
print(jugadorMenorRendimiento(Jugadores))

print("\nJugador más joven:")
print(jugadorMasJoven(Jugadores))

print("\nJugador más veterano:")
print(jugadormasVeterano(Jugadores))

print("\nRanking de jugadores por rendimiento:")
print(rankingJugador(Jugadores))

print("\nPromedio de edad de los jugadores:")
print(promedioEdadJugador(Jugadores))

print("\nPromedio de rendimiento de los jugadores:")
print(promedioRendimientoJugador(Jugadores))