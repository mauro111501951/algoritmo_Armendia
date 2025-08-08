def ejercicio4():
    try:
        n1=int(input("ingrese un numero entero para sumarlo"))
        n2=int(input("ingrese un numero entero para sumarlo"))
        suma=n1+n2
        print(suma)
    except (ValueError, TypeError):
        print("Hola, no")
ejercicio4()