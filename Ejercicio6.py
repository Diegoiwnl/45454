lista = []

def añadir_numero():
    numero = int(input("Ingrese un número para agregar a la lista: "))
    lista.append(numero)
    print(f"El número {numero} ha sido agregado a la lista.")

def añadir_numero_posicion():
    numero = int(input("Ingrese un número para agregar a la lista: "))
    posicion = int(input("Ingrese la posición en la que desea agregar el número (empezando desde 1): "))
    if 1 <= posicion <= len(lista) + 1:
        lista.insert(posicion - 1, numero)
        print(f"El número {numero} ha sido agregado en la posición {posicion} de la lista.")
    else:
        print("La posición ingresada no es válida.")

def longitud_lista():
    print(f"La longitud de la lista es: {len(lista)}")

def eliminar_ultimo_numero():
    if lista:
        ultimo_numero = lista.pop()
        print(f"El último número de la lista ({ultimo_numero}) ha sido eliminado.")
    else:
        print("La lista está vacía.")

def eliminar_numero():
    if lista:
        posicion = int(input("Ingrese la posición del número que desea eliminar (empezando desde 1): "))
        if 1 <= posicion <= len(lista):
            numero_eliminado = lista.pop(posicion - 1)
            print(f"El número {numero_eliminado} ha sido eliminado de la lista.")
        else:
            print("La posición ingresada no es válida.")
    else:
        print("La lista está vacía.")

def contar_numeros():
    numero = int(input("Ingrese un número para contar sus apariciones en la lista: "))
    apariciones = lista.count(numero)
    print(f"El número {numero} aparece {apariciones} veces en la lista.")

def posiciones_numero():
    numero = int(input("Ingrese un número para encontrar sus posiciones en la lista: "))
    posiciones = [i + 1 for i, num in enumerate(lista) if num == numero]
    if posiciones:
        print(f"El número {numero} se encuentra en las posiciones: {', '.join(map(str, posiciones))}")
    else:
        print(f"El número {numero} no está en la lista.")

def mostrar_numeros():
    print("Los números en la lista son:")
    for numero in lista:
        print(numero, end=" ")
    print()

def menu():
    while True:
        print("\nMenú:")
        print("1-Añadir número a la lista")
        print("2-Añadir número de la lista en una posición")
        print("3-Longitud de la lista")
        print("4-Eliminar el último número")
        print("5-Eliminar un número")
        print("6-Contar números")
        print("7-Posiciones de un número")
        print("8-Mostrar números")
        print("9-Salir")

        opcion = input("Seleccione una opción del menú: ")

        if opcion == "1":
            añadir_numero()
        elif opcion == "2":
            añadir_numero_posicion()
        elif opcion == "3":
            longitud_lista()
        elif opcion == "4":
            eliminar_ultimo_numero()
        elif opcion == "5":
            eliminar_numero()
        elif opcion == "6":
            contar_numeros()
        elif opcion == "7":
            posiciones_numero()
        elif opcion == "8":
            mostrar_numeros()
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")


menu()