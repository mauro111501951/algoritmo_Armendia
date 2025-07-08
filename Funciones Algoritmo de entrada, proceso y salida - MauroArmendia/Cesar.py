def Cesar():
    import string

    def obtener_mensaje():
        while True:
            mensaje = input("Ingrese el mensaje a procesar (sin caracteres especiales): ").lower()
            if all(c in string.ascii_lowercase + " " for c in mensaje):
                return mensaje
            else:
                print("No debe incluir caracteres especiales. Intente de nuevo.")

    def cifrar_mensaje(mensaje):
        clave = int(input("Ingrese la clave (número entero): "))
        resultado = ""

        for letra in mensaje:
            if letra == " ":
                resultado += " "
            else:
                nueva_pos = (ord(letra) - ord('a') + clave) % 26
                resultado += chr(ord('a') + nueva_pos)

        return resultado

    def descifrar_mensaje(mensaje):
        clave = int(input("Ingrese la clave (número entero): "))
        resultado = ""

        for letra in mensaje:
            if letra == " ":
                resultado += " "
            else:
                nueva_pos = (ord(letra) - ord('a') - clave) % 26
                resultado += chr(ord('a') + nueva_pos)

        return resultado

    def menu_cesar():
        print("Bienvenido al programa de Cifrado César")
        while True:
            print("\nSeleccione una opción:")
            print("1. Cifrar un mensaje")
            print("2. Descifrar un mensaje")
            print("3. Salir")

            opcion = input("Ingrese su opción (1-3): ")

            if opcion == "1":
                texto = obtener_mensaje()
                cifrado = cifrar_mensaje(texto)
                print(f"Mensaje cifrado: {cifrado}")
            elif opcion == "2":
                texto = obtener_mensaje()
                descifrado = descifrar_mensaje(texto)
                print(f"Mensaje descifrado: {descifrado}")
            elif opcion == "3":
                print("Gracias por usar el programa")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    menu_cesar()