def ejercicio_2(nombre, sexo):

    if sexo.lower() == 'mujer':
        if nombre[0].lower() < 'm':
            return "Grupo A"
        else:
            return "Grupo B"
    elif sexo.lower() == 'hombre':
        if nombre[0].lower() >= 'n':
            return "Grupo A"
        else:
            return "Grupo B"
    else:
        return "Sexo no reconocido"

def nomsex():

    nombre = input("Por favor, ingresa tu nombre: ")
    sexo = input("Por favor, ingresa tu sexo (hombre/mujer): ")

    grupo = ejercicio_2(nombre, sexo)
    print(f"¡Hola {nombre}! Tu grupo es: {grupo}")

nomsex()