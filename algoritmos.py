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
    
    # Llamada inicial a la función recursiva
    quicksort_recursive(0, len(arr) - 1)
    return arr

def ordenarJugadores(Sedes, Jugadores, M):
    equipos = []
    for i in range(1, M+1):
        rendimientosFutbol = []
        rendimientosVolleyball = []
        listaFutbol = Sedes[i]["Equipos"]["Futbol"]
        listaVolleyball = Sedes[i]["Equipos"]["Volleyball"]
        
        for j in listaFutbol:
            rendimientosFutbol.append((Jugadores[j]["Rendimiento"], Jugadores[j]["Edad"], j))
        
        for h in listaVolleyball:
            rendimientosVolleyball.append((Jugadores[h]["Rendimiento"], Jugadores[h]["Edad"], h))
        
        # Ordenar las listas de rendimientos usando quicksort
        rendimientosFutbol = quicksort(rendimientosFutbol)
        rendimientosVolleyball = quicksort(rendimientosVolleyball)
        
        # Actualizar las listas de jugadores en la sede con los jugadores ordenados
        Sedes[i]["Equipos"]["Futbol"] = [j for rendimiento, edad, j in rendimientosFutbol]
        Sedes[i]["Equipos"]["Volleyball"] = [h for rendimiento, edad, h in rendimientosVolleyball]
    
    for u in range(1, M+1):
        equipos.append((Sedes[u]["Ciudad"], "Futbol", Sedes[u]["Equipos"]["Futbol"]))
        equipos.append((Sedes[u]["Ciudad"], "Volleyball", Sedes[u]["Equipos"]["Volleyball"]))
    
    return equipos


# Llamada a la función para ordenar los jugadores dentro de cada equipo
print(ordenarJugadores(Sedes, Jugadores, M))

# Mostrar el resultado
# print(Sedes)