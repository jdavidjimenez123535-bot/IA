def calculadora():
    print("Calculadora simple")
    print("Operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elige una opción (1-4): ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", num1 + num2)
    elif opcion == "2":
        print("Resultado:", num1 - num2)
    elif opcion == "3":
        print("Resultado:", num1 * num2)
    elif opcion == "4":
        if num2 == 0:
            print("Error: división entre cero")
        else:
            print("Resultado:", num1 / num2)
    else:
        print("Opción no válida")

calculadora()