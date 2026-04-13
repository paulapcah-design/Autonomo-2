import random

# Lista de opciones posibles
opciones = ["piedra", "papel", "tijera"]

def obtener_eleccion_usuario():
    """
    Esta función solicita al usuario que ingrese su elección.
    Valida que la opción sea correcta antes de devolverla.
    """
    while True:
        eleccion = input("Elige piedra, papel o tijera: ").lower()
        if eleccion in opciones:
            return eleccion
        else:
            print("Opción inválida. Intenta de nuevo.")


def obtener_eleccion_computadora():
    """
    Esta función genera una elección aleatoria para la computadora
    utilizando la librería random.
    """
    return random.choice(opciones)


def determinar_ganador(usuario, computadora):
    """
    Esta función compara las elecciones del usuario y la computadora
    y determina el resultado del juego.
    Retorna un mensaje indicando si el usuario gana, pierde o empata.
    """
    if usuario == computadora:
        return "Empate"
    
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    
    else:
        return "Perdiste"


def jugar():
    """
    Función principal del juego.
    Controla el flujo del programa usando un bucle while para permitir
    múltiples rondas hasta que el usuario decida salir.
    """
    while True:
        print("\n--- Piedra, Papel o Tijera ---")
        
        # Obtener elecciones
        usuario = obtener_eleccion_usuario()
        computadora = obtener_eleccion_computadora()
        
        # Mostrar elecciones
        print(f"Tú elegiste: {usuario}")
        print(f"La computadora eligió: {computadora}")
        
        # Determinar resultado
        resultado = determinar_ganador(usuario, computadora)
        print(f"Resultado: {resultado}")
        
        # Preguntar si desea seguir jugando
        continuar = input("¿Quieres jugar otra vez? (s/n): ").lower()
        
        if continuar != "s":
            print("Gracias por jugar 👋")
            break


# Ejecutar el juego
jugar()