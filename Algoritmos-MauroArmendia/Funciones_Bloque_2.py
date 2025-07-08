def Ejercicio_1():
    contadorFerra = 0
    contadorVitelli = 0
    contadorMolinas = 0
    votacion = 1
    print("Bienvenido a la votación por el delegado. Hay 3 candidatos:")
    print("Ingrese 1 para votar a Ferra")
    print("Ingrese 2 para votar a Vitelli")
    print("Ingrese 3 para votar a Molinas")
    print("Ingrese 0 para terminar")
    while votacion != 0:
        votacion = int(input("Vota: "))
        if votacion == 0:
            break
        elif votacion == 1:
            contadorFerra += 1
        elif votacion == 2:
            contadorVitelli +=1
        elif votacion == 3:
            contadorMolinas +=1
        else:
            print("Debe ingresar un numero del 0-3")
    if contadorFerra == contadorVitelli or contadorFerra == contadorMolinas or contadorMolinas == contadorVitelli:
        votacion = int(input("Vota para desempatar una sola vez: "))
        if votacion == 1:
            contadorFerra += 1
        elif votacion == 2:
            contadorVitelli +=1
        elif votacion == 3:
            contadorMolinas +=1
    if contadorVitelli > contadorFerra and contadorVitelli > contadorMolinas:
        print("Vitelli ganó.")
        print("------------------------------")
    elif contadorFerra > contadorVitelli and contadorFerra > contadorMolinas:
        print("Ferra ganó.")
        print("------------------------------")
    elif contadorMolinas > contadorFerra and contadorMolinas > contadorVitelli:
        print("Molinas ganó")
        print("------------------------------")
    print("Ferra obtuvo:", contadorFerra, "votos.")
    print("Vitelli obtuvo:", contadorVitelli, "votos.")
    print("Molinas obtuvo:", contadorMolinas, "votos.")


def Ejercicio_2():
    import random
    import string
    contraseña=""
    num = 0
    for i in range(8):
        randomm = random.randint(0,1)
        if randomm == 1:
            num = random.randint(0,9)
            contraseña += str(num)
        else:
            strr = random.choice(string.ascii_letters)
            contraseña += strr  
    print(contraseña)


def Ejercicio_3():
    print("Bienvenido a su agenda de teléfonos ¿Qué desea hacer?")
    print("1: Agregar nuevos contactos")
    print("2: Consultar tus contactos")
    print("3: Salir del programa")
    contactos = []
    telefonos = []
    programa = 0
    contador = 0
    while programa != 3:
        programa = int(input("Ingrese un número: "))
        if programa == 1:
            contacto = str(input("Ingrese el nombre del nuevo contacto: "))
            contactos.append(contacto)
            telefono = int(input("Ingrese el telefono del nuevo contacto: "))
            telefonos.append(telefono)
        elif programa == 2:
            print("Contactos:", contactos)
            buscar = str(input("Ingrese el contacto que desea buscar: "))
            try:
                indice = contactos.index(buscar)
            except ValueError:
                print(f"El elemento {buscar} no se encuentra en la lista.")
            print("El contacto:", contactos[indice])
            print("Tiene por teléfono:", telefonos[indice])
        else:
            break


def Ejercicio_4():
    imp = 0
    num = 0
    while imp < 50:
        if num % 2 == 0 and num % 5 == 0:
            num += 0
        elif num % 2 == 0:
            print(num)
            imp +=1
        elif num % 5 == 0:
            print(num)
            imp +=1
        num +=1


def Ejercicio_5():
    promedio = 0
    for i in range(5):
        nota = int(input("Ingrese sus notas: "))
        promedio += nota
    promedio = promedio/5
    print("El promedio del alumno es:", promedio)
    if promedio >= 6:
        print("El alumno esta aprobado.")
    else:
        print("El alumno está desaprobado.")


def Ejercicio_6():
    import random
    ganaPC = 0
    ganaPJ = 0
    print("Jugaras piedra papel o tijera a 3 rondas: ")
    for i in range(3):
            pc = random.randint(1, 3)
            print("1. Piedra")
            print("2. Papel")
            print("3. Tijera")
            pj = int(input("- "))
            print("")
            print("---------------------------------")
            print("")
            if pc == 1:
                print("PC: Piedra")
            elif pc == 2:
                print("PC: Papel")
            else:
                print("PC: Tijeras")
            if pj == 1:
                print("PJ: Piedra")
            elif pj == 2:
                print("PJ: Papel")
            else:
                print("PJ: Tijeras")
            print("")
            if pc == 1 and pj == 3:
                print("Ganó la PC")
                ganaPC += 1
                print("PC", ganaPC, "- PJ", ganaPJ)
            elif pj == 1 and pc == 3:
                print("Ganó el PJ")
                ganaPJ += 1
                print("PC", ganaPC, "- PJ", ganaPJ)
            elif pc > pj:
                print("Ganó la PC")
                ganaPC += 1
                print("PC", ganaPC, "- PJ", ganaPJ)
            elif pj > pc:
                print("Ganó el PJ")
                ganaPJ += 1
                print("PC", ganaPC, "- PJ", ganaPJ)
            else:
                print("Empate")
                print("PC", ganaPC, "- PJ", ganaPJ)
            print("")
            print("---------------------------------")
            print("")


def Ejercicio_7():
    def invertir_palabra(palabra):
        return palabra[::-1]


    frase = str(input("Ingrese una frase: "))
    palabras = frase.split()
    frase = ""
    for i in range(len(palabras)):
        palabras[i] = invertir_palabra(palabras[i])
    for i in range(len(palabras)):
        frase = frase + " " + palabras[i]
    print(frase)


def Ejercicio_8():
    palabra = str(input("Ingrese una palabra: "))
    letras = []
    for i in palabra:
        if i not in letras:
            letras.append(i)
    for letra in letras:
        cant = palabra.count(letra)
        print("La letra,", letra, "se repite:", cant)


def Ejercicio_9():
    hora = 00
    print(hora)
    for hora in range(0, 24):
        for minuto in range(0, 60):
            print(hora, ":", minuto)


def Ejercicio_10():
    contraseña = "brbrpata"
    usuario = str(input("Ingrese su usuario: "))
    for i in range(3):
        verificar = str(input("Ingrese su contraseña: "))
        if verificar != contraseña:
            print("Contraseña incorrecta.")
        else:
            print("Acceso concedido.")
            print("Bienvenido.")
            break


def Ejercicio_11():
    import random
    sujeto = ["Ferra ", "Vitelli ", "El Chino ", "Nico ", "El Veneco "]
    verbo = ["pateó ", "tomó ", "lanzó ", "atrapó ", "encontró "]
    objeto = ["una pelota", "una cartuchera", "un lapiz", "una botella", "un abrigo"]
    num = random.randint(0,4)
    frase = sujeto[num]
    num = random.randint(0,4)
    frase = frase + verbo[num]
    num = random.randint(0,4)
    frase = frase + objeto[num]
    print(frase)


def Ejercicio_12():
    import math


    print("Modo calculadora cientifica:")
    print("1. Elevar al cuadrado (X^2)")
    print("2. Sacar raiz (√X)")
    print("3. Sacar el seno de x, sin(x)")
    print("4. Sacar el coseno de x, cos(x)")
    operacion = int(input("Ingrese un número del 1-4: "))
    num = int(input("Ingrese X: "))
    res = 0
    if operacion == 1:
        res = num**2
        print(num, "^2 =", res)
    elif operacion == 2:
        res = math.sqrt(num)
        print("√", num, "=", res)
    elif operacion == 3:
        res = math.sin(num)
        print("sin(",num, ") =", res)
    elif operacion == 4:
        res = math.cos(num)
        print("cos(",num, ") =", res)
    else:
        print("Ingrese una de las 4 operaciones permitidas")


def Ejercicio_13():
    num = int(input("Ingrese un número natural: "))
    if num <= 0:
        print("El número debe ser mayor a 0.")
    elif num <= 25:
        print("Su número se encuentra entre 1-25.")
    elif num <= 50:
        print("Su número se encuentra entre 26-50.")
    elif num <= 75:
        print("Su número se encuentra entre 51-75.")
    elif num <= 100:
        print("Su número se encuentra entre 76-100")


def Ejercicio_14():
    peso = float(input("Ingrese su peso en Kg: "))
    altura = float(input("Ingrese su altura en Cm: "))
    altura = altura ** 2
    imc = peso / altura
    if imc < 18.5:
        print("Usted esta por debajo del peso saludable.")
    elif imc < 25:
        print("Usted tiene peso normal.")
    elif imc < 30:
        print("Usted tiene sobrepeso.")
    elif imc > 30:
        print("Usted tiene sobrepeso.")


def Ejercicio_15():
    tareas = []
    restantes = []
    cant = int(input("Ingrese cuantas tareas debe cumplir: "))
    for i in range(cant):
        tarea = str(input("Ingrese sus tareas: "))
        tareas.append(tarea)
    cant = int(input("Ingrese cuantas tareas cumplió: "))
    for i in range(cant):
        tarea = str(input("Ingrese que tarea completo: "))
        tareas.remove(tarea)
    print("Tareas por cumplir:", tareas)


def Ejercicio_16():
    palabra = str(input("Ingrese una palabra: "))
    letra = ""
    for i in palabra:
        letra = letra + str(i)
        print(letra)


def Ejercicio_17():
    rtac = 0
    print("BIENVENIDO A LA FERRATRIVIA")
    print("DEBERAS RESPONDER 3 PREGUNTAS")
    print("PREGUNTA NÚMERO 1:")
    print("Cuál es el Angry Bird con poder de velocidad: ")
    print("1) Rojo")
    print("2) Amarillo")
    print("3) Negro")
    rta = int(input("Ingrese su respuesta: "))
    if rta == 2:
        rtac += 1
        print("Respuesta correcta")
    else:
        print("Respuesta incorrecta")
        print("El pájaro mas rápido es el amarillo.")
    print(" ")
    print("----------------------------------------------")
    print(" ")
    print("En que año ganó boca su primera libertadores: ")
    print("1) 1957")
    print("2) 1967")
    print("3) 1977")
    rta = int(input("Ingrese su respuesta: "))
    if rta == 3:
        rtac += 1
        print("Respuesta correcta")
    else:
        print("Respuesta incorrecta")
        print("Boca ganó su primera libertadores en 1977.")
    print(" ")
    print("----------------------------------------------")
    print(" ")
    print("Hasta que instancia llegó Boca Juniors en su última libertadores: ")
    print("1) Cuartos de final")
    print("2) Fase de grupos")
    print("3) Final")
    rta = int(input("Ingrese su respuesta: "))
    if rta == 3:
        rtac += 1
        print("Respuesta correcta")
    else:
        print("Respuesta incorrecta")
        print("Boca llegó a la Final.")
    print(" ")
    print("----------------------------------------------")
    print(" ")
    print("Usted tuvo:", rtac, "respuestas correctas")


def Ejercicio_18():
    lista1 = []
    lista2 = []
    lista3 = []
    print("Ingrese 5 palabras para la lista 1:")
    for i in range(5):
        pal = str(input(""))
        lista1.append(pal)
    print("Ingrese 5 palabras para la lista 2:")
    for i in range(5):
        pal = str(input(""))
        lista2.append(pal)
    for i in range(5):
        for n in range(5):
            if lista1[i] == lista2[n]:
                lista3.append(lista1[i])
    print("Elementos en común:", lista3)