# Define los datos de los jugadores
Jugadores = {
    1: {"Nombre": "Juan", "Edad": 20, "Rendimiento": 94},
    2: {"Nombre": "Maria", "Edad": 21, "Rendimiento": 94},
    3: {"Nombre": "Pedro", "Edad": 22, "Rendimiento": 21},
    4: {"Nombre": "Ana", "Edad": 23, "Rendimiento": 25},
    5: {"Nombre": "Carlos", "Edad": 24, "Rendimiento": 66},
    6: {"Nombre": "Laura", "Edad": 25, "Rendimiento": 52},
    7: {"Nombre": "Jose", "Edad": 26, "Rendimiento": 48},
    8: {"Nombre": "Luis", "Edad": 27, "Rendimiento": 73},
    9: {"Nombre": "Sara", "Edad": 28, "Rendimiento": 92},
    10: {"Nombre": "Jorge", "Edad": 29, "Rendimiento": 51},
    11: {"Nombre": "Lorena", "Edad": 30, "Rendimiento": 90},
    12: {"Nombre": "Raul", "Edad": 31, "Rendimiento": 100}
}

# Define los datos de las sedes y equipos
Sedes = {
    1: {
        "Ciudad": "Sede Cali",
        "Equipos": {
            "Futbol": [1, 2, 3],       # IDs de jugadores para equipo de Futbol
            "Volleyball": [4, 5, 6]    # IDs de jugadores para equipo de Volleyball
        }
    },
    2: {
        "Ciudad": "Sede Medellin",
        "Equipos": {
            "Futbol": [7, 8, 9],       # IDs de jugadores para equipo de Futbol
            "Volleyball": [10, 11, 12]  # IDs de jugadores para equipo de Volleyball
        }
    }
}
