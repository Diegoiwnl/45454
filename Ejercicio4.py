def main():

    contraseña_correcta = "senacenigraf"


    while True:
        contraseña_ingresada = input("Por favor, ingresa la contraseña: ")

        # Verificar si la contraseña ingresada es correcta
        if contraseña_ingresada == contraseña_correcta:
            print("¡Contraseña correcta! Acceso concedido.")
            break
        else:
            print("Contraseña incorrecta. Por favor ingrese la contraseña nuevamente.")

main()