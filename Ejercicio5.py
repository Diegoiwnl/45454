def calcular_total_con_iva(valor, porcentaje_iva=21):

    total = valor + valor * (porcentaje_iva / 100)
    return total

def main():

    while True:
        try:
            valor = float(input("Por favor, ingresa el valor: "))
            if valor < 0:
                raise ValueError("El valor no puede ser negativo.")
            break
        except ValueError:
            print("Por favor, ingresa un valor válido (número real positivo).")
    
  
    total_con_iva = calcular_total_con_iva(valor)
    print(f"Total con IVA (21%): {total_con_iva}")

    while True:
        try:
            porcentaje_iva_personalizado = float(input("Por favor, ingresa el porcentaje de IVA personalizado (si no ingresas, se aplicará el 21%): "))
            break
        except ValueError:
            print("Por favor, ingresa un valor válido (número real).")

    total_con_iva_personalizado = calcular_total_con_iva(valor, porcentaje_iva_personalizado)
    print(f"Total con IVA ({porcentaje_iva_personalizado}%): {total_con_iva_personalizado}")


main()