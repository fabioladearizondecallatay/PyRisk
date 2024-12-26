# Juego Estratégico de Batalla

Este es un juego de estrategia en el que el jugador organiza tropas y planifica ataques sobre un tablero de territorios. El objetivo es optimizar las combinaciones de tropas y el orden de los ataques para lograr la mayor cantidad de victorias en función de las características del tablero y las reglas definidas.

## Estructura del Proyecto

El proyecto está dividido en varios archivos clave:

### 1. **`main.py`**
   Es el archivo principal donde el jugador interactúa con el juego. A través de este archivo, se pueden:
   - **Actualizar las reglas del juego**, como el número de territorios, el costo de las tropas y si se debe priorizar atacar territorios débiles.
   - **Crear y configurar el tablero**, ingresando los territorios con su defensa y tipo de terreno.
   - **Visualizar el estado actual** de las reglas y el tablero.
   
### 2. **`juego.py`**
   Este archivo contiene la lógica central del juego, donde se calculan las **combinaciones de tropas** y se optimizan los **ataques** para maximizar las victorias. La función `mejor_combinacion()` evalúa las diferentes combinaciones de tropas y selecciona la que ofrece más victorias.

### 3. **`tablero.py`**
   Se encarga de la **creación del tablero dinámico** y la **visualización** de los territorios. El jugador ingresa los datos de los territorios (nombre, defensa y tipo de terreno), que afectan directamente las decisiones estratégicas.

### 4. **`reglas.py`**
   Define las **reglas del juego**, como el costo de las tropas y la posibilidad de priorizar territorios débiles. Estas reglas pueden modificarse desde el archivo `main.py` para ajustar la dificultad y la estrategia.
