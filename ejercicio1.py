
n=int(input("ingrese un numero para ser dividido"))
n1=int(input("ingrese un numero para dividir con el"))

try:
    division=n/n1
    print(division)
except ZeroDivisionError:
    print("¡No se puede dividir por cero")