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

def factorial():
    print("\n[____Factorial____]\n")
    while True:
        while True:
            n = input("\nIngrese el numero que quiere calcular: ")

            try:
                n = int(n) 
                text = "1"   
                r = 1                  
                if (n < 1):
                    print("\nIngrese un numero mayor que 0\n")
                    continue
                for i in range(n):                    
                    r = r * (i + 1)
                    if (i != 0):
                        text = text + "x" + str(i + 1)
                print("\nResultado: " + text + " = " + str(r))
                break         

            except ValueError:
                print("\nIngrese un numero valido\n")

        while True:
            salir = input("\n ¿Calcular otro numero? (s/n):").lower()
            
            if (salir == "s"):
                break
            
            elif (salir == "n"):
                print("\nVolviendo....")
                return
            
            else:
                print("\nIngrese una opcion valida")
        print("-----------------------------------")                


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
            factorial()
        case "5": 
            print("\nTablas\n")
        case "6":
            print("\nCuadrado y cubo\n")
        case "7": 
            print("\nPromedio\n")
        case "8": 
            print("\nMaximo y minimo\n")
        case "9":
            print("\nSaliendo....\n")
        case _:
            print("\nSeleccione una opcion valida\n")

