def Ejercicio_3():
    x = int(input("Ingrese de cuanto quiere el largo de la secuencia Fibonacci: "))
    primer = 0
    segun = 1
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