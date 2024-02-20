def calcular_precio_entrada(edad):
    """
    Calcula el precio de la entrada según la edad del cliente.
    """
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 30000
    else:
        return 50000

def main():
    """
    Función principal que solicita al usuario su edad y muestra el precio de la entrada.
    """
    while True:
        try:
            edad = int(input("Por favor, ingresa tu edad: "))
            if edad < 0:
                raise ValueError("La edad no puede ser negativa.")
            break
        except ValueError:
            print("Por favor, ingresa una edad válida (número entero positivo).")

    precio_entrada = calcular_precio_entrada(edad)
    if precio_entrada == 0:
        print("¡Felicidades! Puedes entrar gratis.")
    else:
        print(f"El precio de la entrada es: {precio_entrada} pesos.")

# Llamar a la función principal para iniciar el programa
main()