def Ejercicio4(): 
    def cantVocales(frase):
        vocales = "aeiou"
        VOCALES = "AEIOU"
        cantMinusculas = 0
        cantMayusculas = 0
        
        for letra in frase:
            if letra in vocales:
                cantMinusculas += 1
            elif letra in VOCALES:
                cantMayusculas += 1
        return cantMinusculas, cantMayusculas

    frase = input("Ingresa una frase: ")
    minusculas, mayusculas = cantVocales(frase)
    print(f"Vocales en minúscula: {minusculas}")
    print(f"Vocales en mayúscula: {mayusculas}")