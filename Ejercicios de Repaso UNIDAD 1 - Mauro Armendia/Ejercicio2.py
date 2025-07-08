def Ejercicio2():
    num = int(input("Ingrese un número natural: "))
    if num > 0:
        for i in range(1, num):
            num = num * i
        print(num)
    else:
        print("Tiene que ser mayor a 0")