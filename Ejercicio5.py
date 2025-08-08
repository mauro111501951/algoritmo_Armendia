def ejercio5():
    try:
        n=int(input("ingrese un numero"))
        n1=int(input("ingrese un numero"))
        division=n/n1
        print(division)
    except (ZeroDivisionError, ValueError):
        print("no es posible hacer el calculo")
    finally:
        print("Fin del calculo")
ejercio5()