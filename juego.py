from itertools import permutations
from reglas import reglas
from tablero import crear_tablero_dinamico

# Generar combinaciones de tropas
def generar_combinaciones():
    combinaciones = []
    puntos_maximos = reglas["puntos_maximos"]
    tropas = reglas["tropas"]
    for inf in range(1, puntos_maximos + 1):  # Al menos 1 infantería, 1 Caballeria y 1 Artilleria
        for cab in range(1, (puntos_maximos // tropas["Caballería"]["Costo"]) + 1):
            for art in range(1, (puntos_maximos // tropas["Artillería"]["Costo"]) + 1):
                costo_total = (inf * tropas["Infantería"]["Costo"] +
                               cab * tropas["Caballería"]["Costo"] +
                               art * tropas["Artillería"]["Costo"])
                if costo_total <= puntos_maximos:
                    combinaciones.append((inf, cab, art))
    return combinaciones


def mejor_combinacion(tablero):
    combinaciones = generar_combinaciones()
    mejor_victoria = 0
    mejor_configuracion = None

    for combinacion in combinaciones:
        victorias, _ = calcular_victorias(combinacion, tablero, list(tablero.keys()))
        if victorias > mejor_victoria:
            mejor_victoria = victorias
            mejor_configuracion = combinacion

    return mejor_configuracion, mejor_victoria

def generar_ordenes(territorios, tablero):
    ordenes_sin_restriccion = list(permutations(territorios))
    if reglas.get("priorizar_debiles", False):
        territorios_ordenados = sorted(territorios, key=lambda t: tablero[t]["Defensa"])
        ordenes_con_restriccion = list(permutations(territorios_ordenados))
    else:
        ordenes_con_restriccion = ordenes_sin_restriccion
    return ordenes_sin_restriccion, ordenes_con_restriccion

# Calcular victoria
def optimizar_ataque(combinaciones, tablero, ordenes_de_ataque):
    mejor_victoria = 0
    mejor_configuracion = None
    mejor_orden = None
    for orden in ordenes_de_ataque:
        for combinacion in combinaciones:
            victorias, _ = calcular_victorias(combinacion, tablero, orden)
            if victorias > mejor_victoria:
                mejor_victoria = victorias
                mejor_configuracion = combinacion
                mejor_orden = orden
    return mejor_configuracion, mejor_orden, mejor_victoria

def calcular_victorias(combinacion, tablero, orden):
    victorias = 0
    fuerza_total = sum(combinacion)  # Suma la fuerza total de las tropas
    for territorio in orden:
        if fuerza_total > tablero[territorio]["Defensa"]:
            victorias += 1  # Cuenta el territorio como conquistado
            fuerza_total -= tablero[territorio]["Defensa"]  # Reduce la fuerza restante
        else:
            break  # Si no puedes conquistar un territorio, detén el ataque
    return victorias, []

# Jugar una partida

def jugar(tablero):
    print("\n--- Jugar una partida ---")
    combinacion_optima, victorias_optimas = mejor_combinacion(tablero)
    print("\n--- Mejor combinación de tropas para maximizar conquistas ---")
    print(f"  Infantería: {combinacion_optima[0]}")
    print(f"  Caballería: {combinacion_optima[1]}")
    print(f"  Artillería: {combinacion_optima[2]}")
    print(f"  Conquistas posibles: {victorias_optimas}")

    # Continuar con las combinaciones, órdenes y optimización del ataque como antes
    combinaciones = generar_combinaciones()
    ordenes_sin_restriccion, ordenes_con_restriccion = generar_ordenes(list(tablero.keys()), tablero)

    # Optimizar ataque con las órdenes sin restricciones
    configuracion_optima, mejor_orden_sin_restriccion, victorias_optimas_sin_restriccion = optimizar_ataque(
        combinaciones, tablero, ordenes_sin_restriccion
    )

    # Mostrar resultados
    mejor_infanteria, mejor_caballeria, mejor_artilleria = configuracion_optima
    print("\n--- Resultado de la partida ---")
    print(f"Mejor combinación de tropas:")
    print(f"  - Infantería: {mejor_infanteria}")
    print(f"  - Caballería: {mejor_caballeria}")
    print(f"  - Artillería: {mejor_artilleria}")
    print(f"Mejor orden de ataque (sin restricciones): {mejor_orden_sin_restriccion}")
    print(f"Total de victorias posibles: {victorias_optimas_sin_restriccion}")

    print("\n--- Jugar una partida ---")
    # Generar combinaciones de tropas
    combinaciones = generar_combinaciones()
    ordenes_sin_restriccion, ordenes_con_restriccion = generar_ordenes(list(tablero.keys()), tablero)

    # Mostrar combinaciones de tropas
    print("\n--- Combinaciones posibles de tropas ---")
    for idx, comb in enumerate(combinaciones, start=1):
        print(f"{idx}. Infantería: {comb[0]}, Caballería: {comb[1]}, Artillería: {comb[2]}")

    # Mostrar permutaciones del orden de ataque sin restricciones
    print("\n--- Permutaciones posibles del orden de ataque (sin restricciones) ---")
    for idx, orden in enumerate(ordenes_sin_restriccion, start=1):
        print(f"{idx}. Orden: {orden}")

    # Optimizar ataque con las órdenes sin restricciones
    configuracion_optima, mejor_orden_sin_restriccion, victorias_optimas_sin_restriccion = optimizar_ataque(
        combinaciones, tablero, ordenes_sin_restriccion
    )

    if reglas.get("priorizar_debiles", False):
        # Optimizar ataque con las órdenes con restricciones
        _, mejor_orden_con_restriccion, victorias_optimas_con_restriccion = optimizar_ataque(
            combinaciones, tablero, ordenes_con_restriccion
        )
    else:
        mejor_orden_con_restriccion = None  # Sin restricciones, no hay un orden alternativo
        victorias_optimas_con_restriccion = None

    # Mostrar resultados
    mejor_infanteria, mejor_caballeria, mejor_artilleria = configuracion_optima
    print("\n--- Resultado de la partida ---")
    print(f"Mejor combinación de tropas:")
    print(f"  - Infantería: {mejor_infanteria}")
    print(f"  - Caballería: {mejor_caballeria}")
    print(f"  - Artillería: {mejor_artilleria}")
    print(f"Mejor orden de ataque (sin restricciones): {mejor_orden_sin_restriccion}")
    print(f"Total de victorias posibles: {victorias_optimas_sin_restriccion}")

    if mejor_orden_con_restriccion:
        print("\nOrden de ataque con restricciones:")
        print(f"  {mejor_orden_con_restriccion}")
        print(f"Total de victorias posibles: {victorias_optimas_con_restriccion}")

#BONUS
def asignar_tropas_por_terreno(tablero, combinacion):
    """
    Asigna tropas a los territorios en función del tipo de terreno y la estrategia definida.
    """
    estrategia_terreno = {
        "Montaña": {"prioridad": ["Artillería", "Infantería"], "peso": {"Artillería": 2, "Infantería": 1}},
        "Llanura": {"prioridad": ["Caballería", "Infantería"], "peso": {"Caballería": 3, "Infantería": 1}},
        "Valle": {"prioridad": ["Infantería", "Caballería"], "peso": {"Infantería": 2, "Caballería": 1}},
    }
    tropas_asignadas = {}
    infanteria, caballeria, artilleria = combinacion

    for territorio, datos in tablero.items():
        tipo_terreno = datos["Terreno"]
        estrategia = estrategia_terreno.get(tipo_terreno, {"peso": {}})
        
        # Asignar tropas según prioridad y peso
        tropas_asignadas[territorio] = {
            "Infantería": min(infanteria, estrategia["peso"].get("Infantería", 0)),
            "Caballería": min(caballeria, estrategia["peso"].get("Caballería", 0)),
            "Artillería": min(artilleria, estrategia["peso"].get("Artillería", 0)),
        }

        # Reducir tropas asignadas de las disponibles
        infanteria -= tropas_asignadas[territorio]["Infantería"]
        caballeria -= tropas_asignadas[territorio]["Caballería"]
        artilleria -= tropas_asignadas[territorio]["Artillería"]

    return tropas_asignadas


def calcular_victorias_con_estrategia(tropas_asignadas, tablero, orden):
    """
    Calcula el número de victorias posibles en función de las tropas asignadas estratégicamente.
    """
    victorias = 0
    for territorio in orden:
        defensa = tablero[territorio]["Defensa"]
        fuerza = sum(tropas_asignadas[territorio].values())
        if fuerza > defensa:
            victorias += 1
        else:
            break
    return victorias


def jugar_con_estrategia(tablero):
    """
    Integra la estrategia en el flujo del juego, calculando victorias en función del tipo de terreno.
    """
    print("\n--- Jugar con estrategia ---")
    # Generar combinaciones de tropas
    combinaciones = generar_combinaciones()
    ordenes_sin_restriccion, _ = generar_ordenes(list(tablero.keys()), tablero)

    # Optimizar ataque con las órdenes sin restricciones
    configuracion_optima, mejor_orden_sin_restriccion, _ = optimizar_ataque(
        combinaciones, tablero, ordenes_sin_restriccion
    )

    # Asignar tropas estratégicamente
    mejor_infanteria, mejor_caballeria, mejor_artilleria = configuracion_optima
    combinacion_optima = (mejor_infanteria, mejor_caballeria, mejor_artilleria)
    tropas_asignadas = asignar_tropas_por_terreno(tablero, combinacion_optima)

    # Calcular victorias con estrategia
    victorias_con_estrategia = calcular_victorias_con_estrategia(tropas_asignadas, tablero, mejor_orden_sin_restriccion)

    # Mostrar resultados
    print("\n--- Resultado con estrategia ---")
    print("Tropas asignadas por territorio:")
    for territorio, tropas in tropas_asignadas.items():
        print(f"  {territorio}: Infantería = {tropas['Infantería']}, Caballería = {tropas['Caballería']}, Artillería = {tropas['Artillería']}")
    print(f"Total de victorias posibles con estrategia: {victorias_con_estrategia}")

