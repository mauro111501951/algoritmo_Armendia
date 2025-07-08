#Ejercicio 1:
def edad (i):
    if i%3==0 and i%5==0:
        print("Si es niño Perry, Si es niña el ornitorrinco")
    elif i%3==0:
        print("Si es niño Perry ")
    elif i%5==0:
        print("Si es niña el ornitorrinco")
    else:
        print(i)
    return edad

def Ejercicio_1():
    import Funciones

    for i in range(1, 31):
        Funciones.edad(i)

#Ejercicio 2:
def numPar (num):
    if num % 2 == 0:
        print("Su número es par")
    else:
        print("Su número es impar")
        num = num ** 2
        print("El cuadrado de su número es ", num)

def Ejercicio_2():
    import Funciones
    num = int(input("Ingrese un número entero: "))
    Funciones.numPar(num)

#Ejercicio 3:
def letra (letra):
    while letra != ".":
        letra = str(input("Ingrese una sola letra en minúscula: "))
        largo = len(letra)
        if letra == "a" or letra =="e" or letra == "i" or letra =="o" or letra =="u":
            print("Su letra es una vocal.")
        elif letra ==".":
            print("Programa finalizado.")
            break
        else:
            print("Su letra es una consonante.")

def Ejercicio_3():
    import Funciones

    letra = "Sandy es el mejor brawler"
    Funciones.letra(letra)

#Ejercicio 4:
def tablas (i):
    for n in range(1,11,1):
        tabla = i * n
        print(tabla)

def Ejercicio_4():
    import Funciones
    tabla = 0
    for i in range(2,6,1):
        Funciones.tablas(i)
        print("-----------------")

#Ejercicio 5:
def Ejercicio_5():
    diaCumple = int(input("Ingrese en formato dd el dia de su nacimiento: "))
    mesCumple = int(input("Ingrese en formato mm el mes de su nacimiento: "))
    diaActual = int(input("Ingrese en formato dd el dia actual: "))
    mesActual = int(input("Ingrese en formato mm el mes actual: "))

    if mesCumple > mesActual:
        print("Todavia no cumpliste años este año.")
    elif mesCumple == mesActual:
        if diaCumple > diaActual:
            print("Todavia no cumpliste años este año.")
        elif diaCumple == diaActual:
            print("Hoy es tu cumpleaños.")
        else:
            print("Ya cumpliste años este año.")
    else:
        print("Ya cumpliste años este año.")

#Ejercicio Extra 1
def factorial(num):
    if num > 0:
        for i in range(1, num):
            num = num * i
        print(num)
    else:
        print("Tiene que ser mayor a 0")

def Ejercicio_Extra_1():
    import Funciones

    num = int(input("Ingrese un número natural: "))
    Funciones.factorial(num)

#Ejercicio Extra 2
def fibonacci(x):
    print(primer)
    print(segun)
    if x % 2 == 0:
        for i in range(2, x, 2):
            primer = primer + segun
            print(primer)
            segun = segun + primer
            print(segun)
    else:
        for i in range(2, x-2, 2):
            primer = primer + segun
            print(primer)
            segun = segun + primer
            print(segun)
        primer = primer + segun
        print(primer)

def Ejercicio_Extra_2():
    import Funciones

    x = int(input("Ingrese de cuanto quiere el largo de la secuencia Fibonacci: "))
    primer = 0
    segun = 1
    Funciones.fibonacci(x)

#Ejercicio Extra 3
def Ejercicio_Extra_3():
    frase = str(input("Ingrese una frase: "))
    print(frase[::-1])

#Ejercicio Extra 4
def Menu(menu):
    if menu == 1:
        print("Hola")
    elif menu == 2:
        print("Adios")
    elif menu > 3:
        print("¡¡¡TIENE QUE SER 1, 2 o 3!!!")
    else: 
        print("Finalizando programa...")

def Ejercicio_Extra_4():
    import Funciones

    menu = 0
    while menu != 3:
        print("Ingrese un número:")
        print("1 - Saludar")
        print("2 - Despedirse")
        print("3 - Terminar Programa")
        menu = int(input())
        Funciones.Menu(menu)
    
#Ejercicio Extra 5
def sumaDigitos():
    while num > 0:
        digito = num % 10
        suma = suma + digito
        num = num // 10

def Ejercicio_Extra_5():
    import Funciones

    num = int(input("Ingrese un número entero: "))
    suma = 0
    Funciones.sumaDigitos()
    print(suma)