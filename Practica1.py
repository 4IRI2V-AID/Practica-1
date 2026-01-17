def sumar(): #Todo mal GG Panchisco
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
                
def tablas(): #Tablas individual y del 1 al 10
    def tablaind():
        while True:
            try:
                num = int(input("\nIngrese un numero para ver su tabla: "))
                if 1 <= num <= 1000:
                    break
                else:
                    print("\nDemasiados caracteres, Escriba un numero mas chico: ")
            except ValueError:
                print("\nIngrese solo numeros")
        print(f"\n[____Tabla del numero {num}____]")
    def alltabla():
                        print("\nColoca una opcion valida  (s/n)")
    def clean():
        print("\nColoca una opcion valida  (s/n)")

    def mop():
        while True:
            print("\n[____Menu Tablas de Multiplicar____] \n1.)  Seleccion de tabla \n2.)  Tablas del 1 al 10 \n3.  Limpiar \n4.)  Volver al menu\n")
            opcion = input("Elige una opcion: ")
            if opcion == "1":
                tablaind()
            elif opcion == "2":
                alltabla()
            elif opcion == "3":
                clean()
            elif opcion == "4":
                print("\nRegresando al menu\n")
                return
                      
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
            tablas()
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

