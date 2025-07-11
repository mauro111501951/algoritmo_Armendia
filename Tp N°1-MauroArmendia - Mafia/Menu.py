import Mafia
import Factorial
import Cesar

from Guia import Ejercicio1
from Guia import Ejercicio2
from Guia import Ejercicio3
from Guia import Ejercicio4
from Guia import Ejercicio5
from Guia import Ejercicio6
from Guia import Ejercicio7

while 0 == 0:
    print("(1) Guía de Repaso")
    print("(2) Calculadora de Factoriales")
    print("(3) Cifrado Cesar")
    print("(4) Mafia")
    print("(0) Para salir del menu.")
    menu = int(input("Ingrese que ejercicios desea corregir: "))
    if menu == 0:
        print("Finalizando programa...")
        break
    elif menu == 1:
        segundoMenu = int(input("Ingrese que ejercicio de la Guia desea corregir del 0 al 7 (0 para regresar al menu): "))
        if segundoMenu == 0:
            break
        elif segundoMenu == 1:
            Ejercicio1.Ejercicio1()
        elif segundoMenu == 2:
            Ejercicio2.Ejercicio2()
        elif segundoMenu == 3:
            Ejercicio3.Ejercicio_3()
        elif segundoMenu == 4:
            Ejercicio4.Ejercicio4()
        elif segundoMenu == 5:
            Ejercicio5.Ejercicio5()
        elif segundoMenu == 6:
            Ejercicio6.Ejercicio6()
        elif segundoMenu == 7:
            Ejercicio7.Ejercicio7()
    elif menu == 2:
        Factorial.Factorial()
    elif menu == 3:
        Cesar.Cesar()
    elif menu == 4:
        Mafia.Mafia()
    else:
        print("Ese número no se encuentra disponible")
        print("Vuelve a intentar")
