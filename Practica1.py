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
        GREEN = "\033[32m"
        RESET = "\033[0m"
        ANCHO = 27
        while True:
            while True:
                try:
                    num = int(input("\nIngrese un numero para ver su tabla: "))
                    if 1 <= num <= 1000:
                        break
                    else:
                        print("\nDemasiados caracteres, Escriba un numero mas chico: ")
                except ValueError:
                    print("\nIngrese solo numeros")
            print(f"""{GREEN}_____________________________{RESET}
{GREEN}|{RESET}{f" Tabla del numero {num} ".center(ANCHO)}{GREEN}|
|___________________________|{RESET}""")
            for i in range(1,11):
                contenido = f"{num} x {i} = {num * i}"
                print(f"{GREEN}|{RESET}{contenido.center(ANCHO)}{GREEN}|{RESET}")
            print(f"{GREEN}|___________________________|{RESET}")

            while True:
                opcion = input("\n1.)  Otra tabla \n2.)  Volver al menu: ")
                if opcion =="1":
                    break
                elif opcion =="2":
                    return
                else:
                    print("\nOpcion invalida, intenta de nuevo")
                  
    def alltabla():
        GREEN = "\033[32m"
        RESET = "\033[0m"
        ANCHO = 27
        for num in range(1, 11):
            print(f"""{GREEN}_____________________________{RESET}
{GREEN}|{RESET}{f" Tabla del {num} ".center(ANCHO)}{GREEN}|
|___________________________|{RESET}""")
            for i in range(1, 11):
                contenido = f"{num} x {i} = {num * i}"
                print(f"{GREEN}|{RESET}{contenido.center(ANCHO)}{GREEN}|{RESET}")
            print(f"{GREEN}|___________________________|{RESET}")
        input("\nPresiona ENTER para volver al menu...")
    def mop():
        while True:
            print("\n[____Menu Tablas de Multiplicar____] \n1.)  Seleccion de tabla \n2.)  Tablas del 1 al 10 \n3.)  Volver al menu\n")
            opcion = input("Elige una opcion: ")
            if opcion == "1":
                tablaind()
            elif opcion == "2":
                alltabla()
            elif opcion == "3":
                print("\nRegresando al menu\n")
                return
            else:
                print("\nOpcion invalida")
    mop()
                      

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


def multiplicacion():
    while True:
        print("\n[____Multiplicacion____] \nIngresa numeros positivos o negativos \nEscribe '=' para obtener el resultado\n")
        total2=1
        while True:
            caracter1 = input("numero o '=': ") 
            if caracter1 == "=":
                print(f"\nEl resultado es: {total2}")
                break
            else:
                try:
                    numero1 = float(caracter1)
                    total2*= numero1
                except ValueError:
                    print("\nError, Ingrese un numero o '='")
        while True:
            salir = input("\n Deseas hacer otra multiplicacion? (s/n):").lower()
            if salir == "s":
                break
            elif salir == "n":
                print("\nRegresando al menu\n")
                return
            else:
                print("\nColoca una opcion valida  (s/n)")    


def division():
    print("\n[____Division____] \n")
    while True:
        print("\nIngresa los números para la división: ")
        while True:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                total1 = (num1 / num2)

                print(f"\nEl resultado es: {total1}")
                break

            except ZeroDivisionError:
                print("\nNo se puede dividir entre 0")
            except ValueError:
                print("\nIngresa valores válidos")

        while True:
            salir = input("\n¿Cálcular otra división? (s/n)").lower()

            if (salir == "s"):
                break

            elif(salir == "n"):
                print("\nVolviendo.... ")
                return

            else:
                print("\nIngrese una opción valida")
        print("-----------------------------------")
        
def Maximo_minimo():
    print("\n[____Calcular maximo y minimo____] \n")    
    print("\nIngrese una serie de numeros y se calculara el maximo y minimo.")    
    while True:
        max_numero = float('-inf')
        min_numero = float('inf')

        while True:
            try: 
                num = input("\nIngrese un numero o n para terminar: ") 
                if (num == "n"): 
                    break
                num = int(num)
                if num > max_numero:
                    max_numero = num
                if num < min_numero:
                    min_numero = num 

            except ValueError:
                print("\nError, Ingrese un numero valido")


        print("El Maximo es",max_numero)
        print("El Minimo es",min_numero)
        
        while True:
                salir = input("\n Deseas ingresar otra serie de numeros? (s/n):").lower()
                if salir == "s":
                    break
                elif salir == "n":
                    print("\nRegresando al menu\n")
                    return
                else:
                    print("\nColoca una opcion valida  (s/n)")

menu = 0
while (menu != "9"):
    menu = input("Menu  \n1.-Suma \n2.-Multiplicacion \n3.-Division \n4.-Factorial \n5.-Tablas de multiplicar \n6.-Cudrado y cubo \n7.-Promedio \n8.-Maximo y minimo \n9.-Salir\nIngrese una opcion: ")
    match menu:
        case "1":
            sumar()
        case "2":
            multiplicacion()
        case "3":
            division()
        case "4": 
            factorial()
        case "5": 
            tablas()
        case "6":
            print("\nCuadrado y cubo\n")
        case "7": 
            print("\nPromedio\n")
        case "8": 
            Maximo_minimo()
        case "9":
            print("\nSaliendo....\n")
        case _:
            print("\nSeleccione una opcion valida\n")



