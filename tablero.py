from reglas import reglas

# Crear el tablero dinámico
def crear_tablero_dinamico():
    print("\nIntroduce los datos de los territorios:")
    tablero = {}
    for i in range(1, reglas["territorios"] + 1):
        nombre = input(f"Nombre del territorio {i}: ")
        while True:
            try:
                defensa = int(input(f"Defensa del {nombre}: "))
                if defensa < 0:
                    raise ValueError("La defensa no puede ser un número negativo.")
                break  # Salir del bucle si la entrada es válida
            except ValueError as e:
                print(f"Error: {e}. Por favor, ingresa un número entero válido.")
        terreno = input(f"Tipo de terreno para {nombre} (ejemplo: Montaña, Llanura, Valle): ")
        tablero[nombre] = {"Defensa": defensa, "Terreno": terreno}
    return tablero

# Mostrar el tablero actual
def mostrar_tablero(tablero):
    if not tablero:
        print("\nNo hay un tablero creado aún. Por favor, crea uno primero.")
    else:
        print("\n--- Tablero actual ---")
        for territorio, datos in tablero.items():
            print(f"{territorio}: Defensa = {datos['Defensa']}, Terreno = {datos['Terreno']}")
