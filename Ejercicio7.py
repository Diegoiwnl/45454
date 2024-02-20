def precio_fruta(fruta, cantidad, precios):
    """
    Calcula el precio total de la fruta a partir del diccionario de precios.
    
    Args:
    fruta (str): Nombre de la fruta.
    cantidad (int): Cantidad de frutas vendidas.
    precios (dict): Diccionario de precios de las frutas.
    
    Returns:
    float: Precio total de la fruta.
    """
    if fruta in precios:
        precio_unitario = precios[fruta]
        precio_total = precio_unitario * cantidad
        return precio_total
    else:
        return None

def main():
    """
    Función principal que maneja las consultas de precios de frutas.
    """
    precios_frutas = {
        'manzana': 2.5,
        'banana': 1.8,
        'naranja': 3.0,
        'pera': 2.0,
        'uva': 4.0
    }
    
    while True:
        fruta = input("Ingrese el nombre de la fruta: ").lower()
        cantidad = int(input("Ingrese la cantidad de frutas vendidas: "))
        
        precio = precio_fruta(fruta, cantidad, precios_frutas)
        
        if precio is not None:
            print(f"El precio total de {cantidad} {fruta}(s) es: ${precio}")
        else:
            print("Lo siento, la fruta ingresada no está en la lista de precios.")
        
        continuar = input("¿Desea hacer otra consulta? (s/n): ").lower()
        if continuar != 's':
            break

# Llamar a la función principal para iniciar el programa
main()