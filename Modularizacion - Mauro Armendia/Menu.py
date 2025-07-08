import Funciones
print("1. Ejercicio 1.py")
print("2. Ejercicio 2.py")
print("3. Ejercicio 3.py")
print("4. Ejercicio 4.py")
print("5. Ejercicio 5.py")
print("6. Ejercicio_Extra_1.py")
print("7. Ejercicio_Extra_2.py")
print("8. Ejercicio_Extra_3.py")
print("9. Ejercicio_Extra_4.py")
print("10. Ejercicio_Extra_10.py")
ejercicio = int(input("Ingrese el ejercicio que desea ejecutar (1-10): "))
if ejercicio == 1:
    Funciones.Ejercicio_1()
elif ejercicio == 2:
    Funciones.Ejercicio_2()
elif ejercicio == 3:
    Funciones.Ejercicio_3()
elif ejercicio == 4:
    Funciones.Ejercicio_4()
elif ejercicio == 5:
    Funciones.Ejercicio_5()
elif ejercicio == 6:
    Funciones.Ejercicio_Extra_1()
elif ejercicio == 7:
    Funciones.Ejercicio_Extra_2()
elif ejercicio == 8:
    Funciones.Ejercicio_Extra_3()
elif ejercicio == 9:
    Funciones.Ejercicio_Extra_4()
elif ejercicio == 10:
    Funciones.Ejercicio_Extra_5()
else:
    print("Reinicie el programa e ingrese un número del 1-10")