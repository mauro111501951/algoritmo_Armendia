def Ejercicio7():
    num = int(input("Ingrese un número entero: "))
    suma = 0
    while num > 0:
        digito = num % 10
        suma = suma + digito
        num = num // 10
    print(suma)