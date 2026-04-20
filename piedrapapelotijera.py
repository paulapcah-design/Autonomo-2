import random

# UNIDAD 4: ESTRUCTURA DE DATOS
opciones = ["piedra", "papel", "tijera"]

# UNIDAD 4: FUNCIONES

def mostrar_titulo():
    """Muestra el título del juego"""
    print("\n--- JUEGO PIEDRA, PAPEL O TIJERA ---")


def mostrar_opciones():
    """Muestra las opciones disponibles (uso de FOR)"""
    print("Opciones disponibles:")
    for i in range(len(opciones)):  # UNIDAD 3: FOR
        print(f"{i + 1}. {opciones[i]}")


def obtener_eleccion_usuario():
    """
    Solicita la elección del usuario.
    Usa WHILE + IF + operadores lógicos
    """
    while True:  # UNIDAD 3: WHILE
        mostrar_opciones()
        eleccion = input("Elige (piedra, papel o tijera): ").lower()

        # UNIDAD 3: CONDICIONALES + OPERADORES LÓGICOS
        if eleccion == "piedra" or eleccion == "papel" or eleccion == "tijera":
            if eleccion in opciones:  # UNIDAD 2: IN
                return eleccion
        else:
            print("❌ Entrada inválida. Intenta nuevamente.\n")


def obtener_eleccion_computadora():
    """Genera una elección aleatoria"""
    return random.choice(opciones)  # UNIDAD 2: MANEJO DE DATOS


def determinar_ganador(usuario, computadora):
    """Determina el resultado del juego (IF anidados)"""

    # Empate
    if usuario == computadora:
        return "Empate"

    # Condiciones para ganar
    if (usuario == "piedra" and computadora == "tijera") or \
       (usuario == "papel" and computadora == "piedra") or \
       (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"

    # Caso contrario
    return "Perdiste"


def jugar():
    """
    Función principal del programa.
    Controla todo el flujo del juego.
    """

    # UNIDAD 3: BUCLE PRINCIPAL (WHILE)
    while True:
        mostrar_titulo()

        # Entrada usuario
        usuario = obtener_eleccion_usuario()

        # Elección computadora
        computadora = obtener_eleccion_computadora()

        # Mostrar resultados
        print(f"\nTú elegiste: {usuario}")
        print(f"La computadora eligió: {computadora}")

        # Determinar ganador
        resultado = determinar_ganador(usuario, computadora)
        print("Resultado:", resultado)

        # Preguntar si desea continuar
        continuar = input("\n¿Quieres jugar otra vez? (s/n): ").lower()

        # Decisión final (como en tu diagrama)
        if continuar != "s":
            print("Fin del juego")
            break

# EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    jugar()
