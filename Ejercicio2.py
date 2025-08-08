def ejercicio2():
    try:
        int(input("ingrese su edad"))
        print("su edad es valida")
    except TypeError:
        print("por favor ingrese un numero valido")
ejercicio2()