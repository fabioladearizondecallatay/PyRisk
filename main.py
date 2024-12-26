from juego import jugar, jugar_con_estrategia
from reglas import mostrar_reglas, modificar_reglas
from tablero import crear_tablero_dinamico, mostrar_tablero

# Submenú para jugar una partida
def menu_jugar(tablero):
    while True:
        print("\n--- Submenú: Jugar una partida ---")
        print("1. Crear un tablero nuevo")
        print("2. Ver el tablero actual")
        print("3. Jugar una partida normal")
        print("4. Jugar con estrategia")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción (0-4): ")

        if opcion == "1":  # Crear un tablero nuevo
            tablero = crear_tablero_dinamico()
        elif opcion == "2":  # Ver el tablero actual
            mostrar_tablero(tablero)
        elif opcion == "3":  # Jugar la partida normal
            if tablero is None:
                print("\nNo hay un tablero creado aún. Por favor, crea un tablero antes de jugar.")
            else:
                jugar(tablero)  # Pasamos el tablero existente a la función jugar
        elif opcion == "4":  # Jugar con estrategia
            if tablero is None:
                print("\nNo hay un tablero creado aún. Por favor, crea un tablero antes de jugar con estrategia.")
            else:
                jugar_con_estrategia(tablero)  # Llamada a la función estratégica
        elif opcion == "0":  # Volver al menú principal
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    return tablero  # Devolvemos el tablero actualizado


# Menú principal
def menu_principal():
    print("\n¡Bienvenido a PyRisk!")
    print("1. Jugar una partida")
    print("2. Conocer las reglas")
    print("3. Modificar las reglas")
    print("0. Salir")
    return input("Selecciona una opción (0-3): ")


if __name__ == "__main__":
    tablero = None  # Inicializamos el tablero como None
    while True:
        opcion = menu_principal()
        if opcion == "1":  # Jugar una partida
            tablero = menu_jugar(tablero)  # Submenú de jugar
        elif opcion == "2":  # Conocer las reglas
            mostrar_reglas()
        elif opcion == "3":  # Modificar las reglas
            modificar_reglas()
        elif opcion == "0":  # Salir
            print("¡Gracias por jugar! Hasta pronto.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
