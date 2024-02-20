import random

def tirar_dado():

    return random.randint(1, 6)

def juego():

    print("¡Vamos a jugar!")
    input("Presiona Enter para iniciar")


    print("¡Es el turno de Álvaro!")
    input("Presiona Enter para ver su resultado...")
    resultado_alvaro = tirar_dado()
    print(f"Álvaro obtuvo: {resultado_alvaro}")

    print("¡Es el turno de Barbara!")
    input("Presiona Enter para ver su resultado...")
    resultado_barbara = tirar_dado()
    print(f"Bárbara obtuvo: {resultado_barbara}")

    print("Calculando al ganador")
    if resultado_alvaro > resultado_barbara:
        print("¡Álvaro gana!")
    elif resultado_alvaro < resultado_barbara:
        print("¡Bárbara gana!")
    else:
        print("¡Es un empate!")


juego()