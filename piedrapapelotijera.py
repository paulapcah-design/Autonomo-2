import random

# Lista de opciones del juego
opciones = ["piedra", "papel", "tijera"]

def mostrar_opciones():
    """
    Esta función muestra las opciones disponibles al usuario
    usando un bucle FOR con la variable i.
    """
    print("Opciones disponibles:")
    for i in range(len(opciones)):  # uso de FOR + variable i
        print(f"{i + 1}. {opciones[i]}")


def obtener_eleccion_usuario():
    """
    Esta función solicita la elección del usuario.
    Usa WHILE para repetir hasta que ingrese un valor válido.
    También utiliza IF, OR e IN para validar la entrada.
    """
    while True:  # uso de WHILE
        mostrar_opciones()
        eleccion = input("Elige (piedra, papel o tijera): ").lower()

        # Validación usando IF + OR + IN
        if eleccion == "piedra" or eleccion == "papel" or eleccion == "tijera":
            if eleccion in opciones:  # uso de IN
                return eleccion
        else:
            print("Entrada inválida, intenta de nuevo.\n")


def obtener_eleccion_computadora():
    """
    Esta función selecciona una opción aleatoria para la computadora.
    """
    return random.choice(opciones)


def determinar_ganador(usuario, computadora):
    """
    Determina el resultado del juego usando estructuras IF.
    """
    if usuario == computadora:
        return "Empate"
    
    if (usuario == "piedra" and computadora == "tijera") or \
       (usuario == "papel" and computadora == "piedra") or \
       (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    
    return "Perdiste"


def jugar():
    """
    Función principal que controla el juego completo.
    Usa WHILE para permitir múltiples rondas.
    """
    while True:  # uso de WHILE
        print("\n--- Juego Piedra, Papel o Tijera ---")

        usuario = obtener_eleccion_usuario()
        computadora = obtener_eleccion_computadora()

        print(f"Tú elegiste: {usuario}")
        print(f"La computadora eligió: {computadora}")

        resultado = determinar_ganador(usuario, computadora)
        print("Resultado:", resultado)

        # Preguntar si quiere continuar
        continuar = input("¿Quieres jugar otra vez? (s/n): ").lower()

        if continuar != "s":
            print("Fin del juego ")
            break


# Ejecutar el programa
jugar()