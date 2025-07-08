def Ejercicio1():
    num = int(input("Ingrese un número: "))
    i = 2
    primo = num - 1
    divisor = False
    while i < primo:
        if num % i == 0:
            divisor = True
        i = i + 1
    if divisor == True:
        print("No es primo")
    else:
        print("Es primo")