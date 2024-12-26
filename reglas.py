# Valores por defecto del juego
reglas = {
    "puntos_maximos": 20,
    "tropas": {
        "Infantería": {"Fuerza": 1, "Costo": 1},
        "Caballería": {"Fuerza": 3, "Costo": 3},
        "Artillería": {"Fuerza": 5, "Costo": 5},
    },
    "territorios": 3,
    "priorizar_debiles": True  #BONUS : regla añadida para priorizar territorios débiles
}

# Mostrar reglas actuales
def mostrar_reglas():
    print("\n--- Reglas actuales del juego ---")
    print(f"Puntos máximos disponibles: {reglas['puntos_maximos']}")
    print("Tropas disponibles:")
    for tropa, datos in reglas["tropas"].items():
        print(f"  - {tropa}: Fuerza = {datos['Fuerza']}, Costo = {datos['Costo']}")
    print(f"Número de territorios enemigos: {reglas['territorios']}")
    print(f"Priorizar ataque a territorios débiles: {'Sí' if reglas['priorizar_debiles'] else 'No'}\n")

# Modificar reglas del juego
def modificar_reglas():
    print("\n--- Modificar reglas del juego ---")
    reglas["puntos_maximos"] = int(input("Introduce los puntos máximos disponibles (actual: 20): "))
    for tropa in reglas["tropas"]:
        print(f"\nModificando {tropa}:")
        reglas["tropas"][tropa]["Fuerza"] = int(input(f"  Nueva fuerza de {tropa} (actual: {reglas['tropas'][tropa]['Fuerza']}): "))
        reglas["tropas"][tropa]["Costo"] = int(input(f"  Nuevo costo de {tropa} (actual: {reglas['tropas'][tropa]['Costo']}): "))
    reglas["territorios"] = int(input(f"\nIntroduce el número de territorios enemigos (actual: 3): "))
    
    # Añadir opción para activar/desactivar la nueva regla
    respuesta = input("\n¿Activar la prioridad de atacar territorios débiles? (sí/no, actual: {}): ".format(
        "Sí" if reglas["priorizar_debiles"] else "No")).strip().lower()
    if respuesta in ("sí", "si"):
        reglas["priorizar_debiles"] = True
    elif respuesta == "no":
        reglas["priorizar_debiles"] = False

    print("\n¡Reglas actualizadas correctamente!")
