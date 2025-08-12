def ejercio1 ():
   plata=1000
   while 0 == 0:
      print("seleccione que accion quiere realizar")
      print("1. Depositar dinero")
      print("2. Retirar dinero")
      print("3. Salir")
      menu = int(input(""))
      if menu==1:
        try:
             deposito = float(input("¿Cuanto dinero quiere depositar?"))
             plata= plata + deposito
             print("Este es su saldo total", plata) 
        except ValueError:
           print("No se pueden ingresar otra cosa que no sean numeros")
      if menu == 2:
         print("Saldo disponible:", plata)
         try:
            retiro = float(input("Ingrese la cantidad que desea retirar"))
            plata= plata - retiro
            print(" Este es el saldo que le quedo:", plata)
            if retiro > plata:
               print(" No se puede retirar una cantidad mayor al saldo")
         except ValueError:
            print("No se puede retirar letras o palabras")
      if menu == 3:
         print("Cerrando el programa")
         break
ejercio1()

def ejercicio2 ():
   try:
      n1=float(input("Ingrese su peso"))
      n2=float(input("Ingrese su altura"))
      Imc=n1/n2**2
      if Imc<18.5:
         print("Usted tiene bajo peso")
      elif Imc>18.5 and Imc<24.5:
         print("Usted tiene un peso saludable")
      elif Imc>25.0 and Imc<29.9:
         print("Usted tiene sobrepeso")
      else:
         print("Usted tiene obesidad")
   except ValueError:
      print("Ingrese un valor apropiado")
ejercicio2()