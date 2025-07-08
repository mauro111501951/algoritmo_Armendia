#Ejercicio 1
def Ejercicio_1():
    for i in range(3, 100, 3):
        print(i)


#Ejercicio 2
def Ejercicio_2():
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Tienes mas de 18 años.")
    elif edad == 18:
        print("Tienes 18 años.")
    else:
        print("Tienes menos de 18 años.")


#Ejercicio 3
def Ejercicio_3():
    palabra = str(input("Ingrese una palabra"))
    letras = 0
    for i in palabra:
        letras += 1
    print(palabra, "tiene", letras, " letras")


#Ejercicio 4
def Ejercicio_4():
    contraseña = "Brr brr patapim"
    adivino = False
    for i in range(3):
        adivinar = str(input("Intente adivinar la contraseña: "))
        if adivinar != contraseña:
            print("Incorrecto")
        else:
            print("Correcto")
            break


#Ejercicio 5
def Ejercicio_5():
    masAlto = 0
    for i in 10:
        num = int(input("Ingrese un número: "))
        if num > masAlto:
            masAlto = num
    print("El número mas alto fue:", masAlto)


#Ejercicio 6
def Ejercicio_6():
    import string
    nombre = str(input("Ingrese su nombre: "))
    print("Hola", nombre.capitalize())


#Ejercicio 7
def Ejercicio_7():
    for i in range(7, 71, 7):
        print(i)


#Ejercicio 8
def Ejercicio_8():
    for i in range(10, 0, -1):
        print(i)
    print("oa")


#Ejercicio 9
def Ejercicio_9():
    num = int(input("Ingrese un número"))
    if num % 2 == 0:
        print("Es par.")
    else:
        print("Es impar.")


#Ejercicio 10
def Ejercicio_10():
    def cantVocales(frase):
        import string

        vocales = "aeiou"
        cantMinusculas = 0
        
        for letra in frase:
            if letra in vocales:
                cantMinusculas += 1
        return cantMinusculas

    frase = input("Ingresa una frase: ")
    frase = frase.lower()
    minusculas = cantVocales(frase)
    print(f"Cantidad de vocales: {minusculas}")


#Ejercicio 11
def Ejercicio_11():
    num = float(input("Ingrese un número para obtener su tabla de multiplicar hasta el 12: "))
    for i in range(1, 13):
        num = num*i
        print(num)
        num = num/i

#Ejercicio 12
def Ejercicio_12():
    num = 0
    while num < 100:
        num = num + int(input("Ingrese un número: "))



#Ejercicio 13
def Ejercicio_13():
    palabra = str(input("Ingrese una palabra: "))
    for i in palabra:
        print(i)


#Ejercicio 14
def Ejercicio_14():
    edad = int(input("Ingrese su edad: "))
    if edad < 16:
        print("No puede manejar ni votar")
    elif edad < 18:
        print("Puede manejar, no puede votar.")
    else:
        print("Puede manejar y votar")


#Ejercicio 15
def Ejercicio_15():
    for i in range(50, 4, -5):
        print(i)


#Ejercicio 16
def Ejercicio_16():
    contraseña = str(input("Ingrese una contraseña: "))
    while 0 == 0:
        verificar = str(input("Ingrese nuevamente su contraseña: "))
        if verificar == contraseña:
            print("Acceso concedido.")
            break
        else:
            print("Acceso denegado, vuelve a intentarlo.")


#Ejercicio 17
def Ejercicio_17():
    while 0 == 0:
        nombre = str(input("Ingrese un nombre: "))
        if len(nombre) >= 10:
            break


#Ejercicio 18
def Ejercicio_18():
    import time
    
    for i in range(61):
        print(i)
        time.sleep(1)
    print("Paso un minuto")


#Ejercicio 19
def Ejercicio_19():
    def cantVocales(frase):
        import string

        vocales = "a"
        cantMinusculas = 0
        
        for letra in frase:
            if letra in vocales:
                cantMinusculas += 1
        return cantMinusculas

    frase = input("Ingresa una frase: ")
    frase = frase.lower()
    minusculas = cantVocales(frase)
    print(f"A's en la oración: {minusculas}")
