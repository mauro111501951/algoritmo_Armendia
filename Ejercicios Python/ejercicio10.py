edad = int(input("Ingrese su edad: "))
pochoclos = str(input("¿Ha comprado pocholos? (responder con si o no): "))
if edad > 65 and pochoclos == "si":
    print("¡Felicidades! Tienes entrada gratuita al cine.")
else:
    print("Compra la entrada o rajá de acá.")
