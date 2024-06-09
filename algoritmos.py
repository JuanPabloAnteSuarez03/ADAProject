from datos import *
import statistics
def equipoMayorRendimiento(Sedes, M):
    mayor = 0
    equipo = ""
    ciudad = ""
    for i in range(1, M+1):
        mediaFutbol = []
        mediaVolleyball = []
        listaFutbol = Sedes[i]["Equipos"]["Futbol"]
        listaVolleyball = Sedes[i]["Equipos"]["Volleyball"]
        for j in listaFutbol:
            mediaFutbol.append(Jugadores[j]["Rendimiento"])
        for h in listaVolleyball:
            mediaVolleyball.append(Jugadores[h]["Rendimiento"])
        promedio_futbol = statistics.mean(mediaFutbol)
        promedio_volleyball = statistics.mean(mediaVolleyball)        
        maximo = max(promedio_futbol, promedio_volleyball)
        if maximo > mayor:
            mayor = maximo
            equipo = "Futbol" if maximo == promedio_futbol else "Volleyball"
            ciudad = Sedes[i]["Ciudad"]
    return mayor, equipo, ciudad

def equipoMenorRendimiento(Sedes, M):
    menor = float('inf')
    equipo = ""
    ciudad = ""
    for i in range(1, M+1):
        mediaFutbol = []
        mediaVolleyball = []
        listaFutbol = Sedes[i]["Equipos"]["Futbol"]
        listaVolleyball = Sedes[i]["Equipos"]["Volleyball"]
        for j in listaFutbol:
            mediaFutbol.append(Jugadores[j]["Rendimiento"])
        for h in listaVolleyball:
            mediaVolleyball.append(Jugadores[h]["Rendimiento"])
        promedio_futbol = statistics.mean(mediaFutbol)
        promedio_volleyball = statistics.mean(mediaVolleyball)        
        minimo = min(promedio_futbol, promedio_volleyball)
        if minimo < menor:
            menor = minimo
            equipo = "Futbol" if minimo == promedio_futbol else "Volleyball"
            ciudad = Sedes[i]["Ciudad"]
    return menor, equipo, ciudad

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
        
        # Ordenar las listas de rendimientos usando quicksort
        rendimientosFutbol = quicksort(rendimientosFutbol)
        rendimientosVolleyball = quicksort(rendimientosVolleyball)
        
        # Actualizar las listas de jugadores en la sede con los jugadores ordenados
        Sedes[i]["Equipos"]["Futbol"] = [j for rendimiento, j in rendimientosFutbol]
        Sedes[i]["Equipos"]["Volleyball"] = [h for rendimiento, h in rendimientosVolleyball]
    
    return Sedes


def ordenarEquipos(Sedes, Jugadores, M):
    # Ordenar los jugadores dentro de cada equipo
    Sedes = ordenarJugadores(Sedes, Jugadores, M)
    
    sedes_ordenadas = []
    
    for i in range(1, M+1):
        sede = Sedes[i]
        equipos_rendimiento = []
        
        for equipo in sede["Equipos"]:
            rendimientos = [Jugadores[j]["Rendimiento"] for j in sede["Equipos"][equipo]]
            promedio_rendimiento = statistics.mean(rendimientos)
            equipos_rendimiento.append((promedio_rendimiento, equipo, sede["Equipos"][equipo]))
        
        # Ordenar los equipos por rendimiento promedio en orden descendente
        equipos_rendimiento = quicksort(equipos_rendimiento)
        equipos_rendimiento.reverse()  # Invertir para tener orden descendente
        
        # Crear una lista con los equipos ordenados
        equipos_ordenados = [(equipo, jugadores) for _, equipo, jugadores in equipos_rendimiento]
        
        # Añadir la sede con los equipos ordenados a la lista
        sedes_ordenadas.append((sede["Ciudad"], equipos_ordenados))
    
    return sedes_ordenadas

def ordenarSedes(Sedes, Jugadores, M):
    # Ordenar los jugadores dentro de cada equipo
    Sedes = ordenarJugadores(Sedes, Jugadores, M)
    
    sedes_ordenadas = []
    
    for i in range(1, M+1):
        sede = Sedes[i]
        equipos_rendimiento = []
        
        for equipo in sede["Equipos"]:
            rendimientos = [Jugadores[j]["Rendimiento"] for j in sede["Equipos"][equipo]]
            promedio_rendimiento = statistics.mean(rendimientos)
            equipos_rendimiento.append((promedio_rendimiento, equipo, sede["Equipos"][equipo]))
        
        # Ordenar los equipos por rendimiento promedio en orden descendente
        equipos_rendimiento = quicksort(equipos_rendimiento)
        equipos_rendimiento.reverse()  # Invertir para tener orden descendente
        
        # Crear una lista con los equipos ordenados
        equipos_ordenados = [(equipo, jugadores) for _, equipo, jugadores in equipos_rendimiento]
        
        # Añadir la sede con los equipos ordenados a la lista
        sedes_ordenadas.append((sede["Ciudad"], equipos_ordenados))
    
    # Ordenar las sedes por el promedio de rendimiento de sus equipos
    sedes_ordenadas = quicksort(sedes_ordenadas)
    sedes_ordenadas.reverse()  # Invertir para tener orden descendente
    
    return sedes_ordenadas

print(ordenarJugadores(Sedes, Jugadores, M))
print(ordenarEquipos(Sedes, Jugadores, M))
print(ordenarSedes(Sedes, Jugadores, M))