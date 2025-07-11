def Mafia():
    import random
    jugador1 = str(input("ingrese el nomre del jugador numero 1 (Ingresa nulo bajo tu propio riesgo): "))
    jugador2 = str(input("ingrese el nomre del jugador numero 2 (Ingresa nulo bajo tu propio riesgo): "))
    jugador3 = str(input("ingrese el nomre del jugador numero 3 (Ingresa nulo bajo tu propio riesgo): "))
    jugador4 = str(input("ingrese el nomre del jugador numero 4 (Opcional): "))
    listavacia = []

    if jugador1 == "":
        jugador1 = "Balatro Balatrez"

    if jugador2 == "":
        jugador2 = "Tralalelo Tralala"

    if jugador3 == "":
        jugador3 = "Lucas Janson"

    if jugador4 == "":
        jugadores = [jugador1, jugador2, jugador3]
        roles = ["Asesino", "Policia", "Civil"]
    else:
        jugadores = [jugador1, jugador2, jugador3, jugador4]
        roles = ["Asesino", "Policia", "Civil", "Civil"]

    rolJugador1 = random.choice(roles)
    for rol in roles:
        if rolJugador1 == rol:
            listavacia.append(rol)
            roles.remove(rol)

    rolJugador2 = random.choice(roles)
    for rol in roles:
        if rolJugador2 == rol:
            listavacia.append(rol)
            roles.remove(rol)

    rolJugador3 = random.choice(roles)
    for rol in roles:
        if rolJugador3 == rol:
            listavacia.append(rol)
            roles.remove(rol)

    if jugador4 != "":
        rolJugador4 = random.choice(roles)
        for rol in roles:
            if rolJugador4 == rol:
                listavacia.append(rol)
                roles.remove(rol)

    print(jugador1)
    revelar = str(input("Presione enter para ver su rol: "))
    print("Usted es:", rolJugador1)
    revelar = str(input("Ingrese enter para llamar al siguiente jugador: "))

    print(jugador2)
    revelar = str(input("Presione enter para ver su rol: "))
    print("Usted es:", rolJugador2)
    revelar = str(input("Ingrese enter para llamar al siguiente jugador: "))

    print(jugador3)
    revelar = str(input("Presione enter para ver su rol: "))
    print("Usted es:", rolJugador3)
    revelar = str(input("Ingrese enter para llamar al siguiente jugador: "))

    print(jugador4)
    revelar = str(input("Presione enter para ver su rol: "))
    print("Usted es:", rolJugador4)
    revelar = str(input("Ingrese enter para cerrar y comenzar el juego: "))