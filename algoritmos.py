from datos import *
import statistics
def mayorRendimiento(Sedes, M):
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

def menorRendimiento(Sedes, M):
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

print(mayorRendimiento(Sedes, M))
print(menorRendimiento(Sedes, M))