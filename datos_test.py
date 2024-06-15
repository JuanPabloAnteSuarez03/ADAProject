# Definición de la clase Jugador
class Jugador:
    def __init__(self, nombre, edad, rendimiento):
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

# Definición de la clase Equipo
class Equipo:
    def __init__(self, deporte, jugadores):
        self.deporte = deporte
        self.jugadores = jugadores

# Definición de la clase Sede
class Sede:
    def __init__(self, ciudad, equipos):
        self.ciudad = ciudad
        self.equipos = equipos

# Creación de los jugadores
j1 = Jugador("Sofia Garcia", 21, 66)
j2 = Jugador("Alejandro Torres", 27, 24)
j3 = Jugador("Valentina Rodriguez", 19, 15)
j4 = Jugador("Juan Lopez", 22, 78)
j5 = Jugador("Martina Martinez", 30, 55)
j6 = Jugador("Sebastian Perez", 25, 42)
j7 = Jugador("Camila Fernandez", 24, 36)
j8 = Jugador("Mateo Gonzalez", 29, 89)
j9 = Jugador("Isabella Diaz", 21, 92)
j10 = Jugador("Daniel Ruiz", 17, 57)
j11 = Jugador("Luciana Sanchez", 18, 89)
j12 = Jugador("Lucas Vasquez", 26, 82)

# Creación de los equipos
e1 = Equipo("Futbol", [j10, j2])
e2 = Equipo("Volleyball", [j1, j9, j12, j6])
e3 = Equipo("Futbol", [j11, j8, j7])
e4 = Equipo("Volleyball", [j3, j4, j5])

# Creación de las sedes
s1 = Sede("Sede Cali", [e1, e2])
s2 = Sede("Sede Medellin", [e3, e4])

# Listas globales para ser utilizadas en el script principal
Jugadores = [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12]
Sedes = [s1, s2]
