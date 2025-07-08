def Ejercicio6():
    menu = 0
    while menu != 3:
        print("Ingrese un número:")
        print("1 - Saludar")
        print("2 - Despedirse")
        print("3 - Terminar Programa")
        menu = int(input())
        if menu == 1:
            print("Hola")
        elif menu == 2:
            print("Adios")
        elif menu > 3:
            print("¡¡¡TIENE QUE SER 1, 2 o 3!!!")
        else: 
            print("Finalizando programa...")
            break