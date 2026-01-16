menu = 0
while (menu != "9"):
    menu = input("Menu  \n1.-Suma \n2.-Multiplicacion \n3.-Division \n4.-Factorial \n5.-Tablas de multiplicar \n6.-Cudrado y cubo \n7.-Promedio \n8.-Mayor y minimo \n9.-Salir\nIngrese una opcion: ")
    match menu:
        case "1":
            print("\nSuma\n")
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
        case "7": 
            print("\nPromedio\n")
        case "8": 
            print("\nMaximo y minimo\n")
        case "9":
            print("\nSaliendo....\n")
        case _:
            print("\nSeleccione una opcion valida\n")
