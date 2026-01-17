def sumar(): #Todo mal GG
    while True:
        print("\n[____Suma____] \nIngresa numeros positivos o negativos \nEscribe '=' para obtener el resultado\n")
        total=0
        while True:
            caracter = input("numero o '=': ") 
            if caracter == "=":
                print(f"\nEl resultado es: {total}")
                break
            else:
                try:
                    numero = float(caracter)
                    total += numero
                except ValueError:
                    print("\nError, Ingrese un numero o '='")
        while True:
            salir = input("\n Deseas hacer otra suma? (s/n):").lower()
            if salir == "s":
                break
            elif salir == "n":
                print("\nRegresando al menu\n")
                return
            else:
                print("\nColoca una opcion valida  (s/n)")
def cuadradoycubo():
    import math
    import os
    def limpiar():
        if os.name == "nt":
            os.system("cls")
    opcion=0
    while opcion!=1:
        limpiar()
        print("Cálculo del cuadrado y cubo de un número")
        num=int(input("\nIngresa un número: "))
        cuadrado=num**2
        cubo=num**3
        print("\nEl cuadrado y cubo del número ingresado es:\nCuadrado: ", cuadrado, "\nCubo: ", cubo)
        opcion = int(input("\nEscribe 1 para salir, escribe otro número para continuar: "))
menu = 0
while (menu != "9"):
    menu = input("Menu  \n1.-Suma \n2.-Multiplicacion \n3.-Division \n4.-Factorial \n5.-Tablas de multiplicar \n6.-Cudrado y cubo \n7.-Promedio \n8.-Mayor y minimo \n9.-Salir\nIngrese una opcion: ")
    match menu:
        case "1":
            sumar()
        case "2":
            print("\nMultiplicacion\n")
        case "3":
            print("\nDivision\n")
        case "4": 
            print("\nFactorial\n")
        case "5": 
            print("\nTablas\n")
        case "6":
            print("\nCuadrado y cubo\n")
            cuadradoycubo()
        case "7": 
            print("\nPromedio\n")
        case "8": 
            print("\nMaximo y minimo\n")
        case "9":
            print("\nSaliendo....\n")
        case _:
            print("\nSeleccione una opcion valida\n")

