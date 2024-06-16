import random
import string
import time
from quickSort import *

# Función para generar un nombre aleatorio
def generar_nombre():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))

# Función para generar datos ficticios
def generar_datos(num_sedes, num_equipos_por_sede, num_jugadores_por_equipo):
    Sedes = {}
    Jugadores = {}
    jugador_id = 1
    
    for sede_id in range(1, num_sedes + 1):
        sede_nombre = f"Sede {sede_id}"
        Sedes[sede_id] = {
            "Ciudad": sede_nombre,
            "Equipos": {
                "Futbol": [],
                "Volleyball": []
            }
        }
        
        for equipo in Sedes[sede_id]["Equipos"]:
            for _ in range(num_jugadores_por_equipo):
                rendimiento = random.randint(1, 100)
                edad = random.randint(18, 40)
                nombre = generar_nombre()
                Jugadores[jugador_id] = {
                    "Rendimiento": rendimiento,
                    "Edad": edad,
                    "Nombre": nombre
                }
                Sedes[sede_id]["Equipos"][equipo].append(jugador_id)
                jugador_id += 1
    
    return Sedes, Jugadores

# Pruebas de rendimiento
print("Analisis de M (Número de Sedes)")
num_equipos_por_sede = 10
num_jugadores_por_equipo = 20
M = 50
for i in range(4):
    Sedes, Jugadores = generar_datos(M, num_equipos_por_sede, num_jugadores_por_equipo)
    tiempo_inicio = time.time()
    ordenarSedes(Sedes, Jugadores, M)
    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicio
    print(f'M = {M}')
    print(f'El tiempo de ejecución para M fue: {tiempo_ejecucion} segundos')
    M *= 3

print("\nAnalisis de K (Número de Equipos por Sede)")
num_sedes = 50
num_jugadores_por_equipo = 20
K = 10
for i in range(4):
    Sedes, Jugadores = generar_datos(num_sedes, K, num_jugadores_por_equipo)
    tiempo_inicio = time.time()
    ordenarSedes(Sedes, Jugadores, num_sedes)
    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicio
    print(f'K = {K}')
    print(f'El tiempo de ejecución para K fue: {tiempo_ejecucion} segundos')
    K *= 3

print("\nAnalisis de N (Número de Jugadores por Equipo)")
num_sedes = 50
num_equipos_por_sede = 10
N = 20
for i in range(4):
    Sedes, Jugadores = generar_datos(num_sedes, num_equipos_por_sede, N)
    tiempo_inicio = time.time()
    ordenarSedes(Sedes, Jugadores, num_sedes)
    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicio
    print(f'N = {N}')
    print(f'El tiempo de ejecución para N fue: {tiempo_ejecucion} segundos')
    N *= 3
