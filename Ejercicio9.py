def guardar_notas():

    num_alumnos = int(input("Ingrese el número de alumnos: "))
    datos_alumnos = {}

    for _ in range(num_alumnos):
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        notas = []

        while True:
            nota = float(input(f"Ingrese la nota del alumno {nombre_alumno} (ingrese un número negativo para terminar): "))
            if nota < 0:
                break
            notas.append(nota)

        if nombre_alumno in datos_alumnos:
            print(f"Error: El nombre '{nombre_alumno}' ya existe en la lista.")
        else:
            datos_alumnos[nombre_alumno] = notas
    
    return datos_alumnos

def calcular_media_notas(datos_alumnos):

    print("\nLista de alumnos y notas medias:")
    for alumno, notas in datos_alumnos.items():
        if notas:
            media = sum(notas) / len(notas)
            print(f"{alumno}: {notas} - Nota media: {media:.2f}")
        else:
            print(f"{alumno}: No tiene notas registradas")

def main():

    print("Bienvenido al programa de registro de notas de alumnos.")
    datos_alumnos = guardar_notas()
    calcular_media_notas(datos_alumnos)


main()