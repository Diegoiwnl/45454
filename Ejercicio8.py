def crear_cesta_compra():
    """
    Crea un diccionario simulando una cesta de la compra.
    """
    cesta_compra = {}
    
    while True:
        articulo = input("Ingrese el nombre del artículo ('fin' para terminar): ")
        if articulo.lower() == 'fin':
            break
        try:
            precio = float(input("Ingrese el precio del artículo: "))
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
        except ValueError:
            print("Error: por favor, ingrese un precio válido (número real positivo).")
            continue
        
        cesta_compra[articulo] = precio
    
    return cesta_compra

def mostrar_cesta_y_coste(cesta_compra):
    """
    Muestra por pantalla la lista de la compra y el coste total.
    
    Args:
    cesta_compra (dict): Diccionario que representa la cesta de la compra.
    """
    if not cesta_compra:
        print("La cesta de la compra está vacía.")
        return
    
    print("Lista de la compra:")
    total_coste = 0
    for articulo, precio in cesta_compra.items():
        print(f"{articulo}: ${precio}")
        total_coste += precio
    
    print(f"Coste total: ${total_coste}")

def main():
    """
    Función principal que gestiona la creación de la cesta de la compra y muestra su contenido y coste total.
    """
    print("Bienvenido a la cesta de la compra. Por favor, ingrese los artículos y sus precios.")
    cesta_compra = crear_cesta_compra()
    print("\nContenido de la cesta de la compra:")
    mostrar_cesta_y_coste(cesta_compra)

# Llamar a la función principal para iniciar el programa
main()