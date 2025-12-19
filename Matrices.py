import random

nombres = [
    "Agustín", "Milagros", "Franco", "Catalina", "Tobías", "Abril", "Renzo", "Malena", "Bautista", "Elena",
    "Nicolás", "Lara", "Juan", "Josefina", "Ramiro", "Guadalupe", "Facundo", "Delfina", "Emiliano", "Roma",
    "Pablo", "Miranda", "Marcos", "Naiara", "Axel", "Florencia", "Kevin", "Sol", "Nahuel", "Alma",
    "Jeremías", "Pilar", "Ulises", "Ana", "Santino", "Eva", "Mauricio", "Candela", "Rodrigo", "Jazmín",
    "Cristóbal", "Selena", "Ezequiel", "Uma", "Valentín", "Helena", "Orlando", "Violeta", "Alan", "Guillermina"
]


posiciones = [
    "Delantero", "Mediocampista", "Defensor", "Arquero"
]

def Crear_Equipo():
    filas, columnas = 23, 1
    matriz_jugadores = []
    matriz_nombres = [[random.choice(nombres) for _ in range(columnas)] for _ in range(filas)]
    matriz_posicion = [[random.choice(posiciones) for _ in range(columnas)] for _ in range(filas)]
    matriz_media = [[random.randint(50, 100) for _ in range(columnas)] for _ in range(filas)]
    matriz_jugadores.append(matriz_nombres)
    matriz_jugadores.append(matriz_posicion)
    matriz_jugadores.append(matriz_media)
    return matriz_jugadores

def Calcular_Promedio():
    Equipo = Crear_Equipo()
    promedio = 0
    for fila in Equipo[2]:
        for elemento in fila:
            promedio += elemento
    promedio = promedio // 23
    return promedio

Promedio1 = Calcular_Promedio()
Promedio2 = Calcular_Promedio()

if Promedio1 > Promedio2:
    print(f"Media Equipo 1: {Promedio1}")
    print(f"Media Equipo 2: {Promedio2}")
    print("El equipo ganador es el equipo 1.")
elif Promedio2 > Promedio1:
    print(f"Media Equipo 1: {Promedio1}")
    print(f"Media Equipo 2: {Promedio2}")
    print("El equipo ganador es el equipo 2.")
else:
    print(f"Media Equipo 1: {Promedio1}")
    print(f"Media Equipo 2: {Promedio2}")
    print("Es un empate.")