def Factorial ():
    fact = 1
    for i in range(3, 0, -1):
        print("Te quedan", i, "intentos.")
        num = int(input("Ingrese un número para obtener su factorial: "))
        if num > 0:
            for i in range(1, num+1):
                fact *= i
            print(num,"! =", fact)
            break
        else:
            print("Numero no válido.")
            print("Intente nuevamente.")
            i += 1