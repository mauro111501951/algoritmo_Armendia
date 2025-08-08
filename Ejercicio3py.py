def ejercicio3():
    try:
        list=["Ana","Pedro","Sofia"]
        n1=int(input("ingrese un numero del 0 a 2 para seleccionar un numero"))
        print(list[n1])
    except IndexError:
        print("Ingrese un numero que este dentro del rango")
ejercicio3()