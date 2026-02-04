# Tic-Tac-Toe CLI (Python)

Juego de Tres en Raya en consola (CLI) hecho en Python.

- El jugador usa **'O'**
- La CPU usa **'X'**
- La CPU empieza colocando **'X' en el centro** (casilla 5)
- El jugador elige casilla introduciendo un número del **1 al 9**

## Requisitos

- Python 3.x

## Cómo ejecutar

```bash
python main.py
```

## Cómo jugar

- Cuando sea tu turno, escribe un número del 1 al 9 para elegir una casilla libre.

- El juego valida:

  -> que sea un número

  -> que esté en rango 1–9

  -> que la casilla esté libre

## Estructura del código

- Funciones principales:

  -> display_board(board): muestra el tablero en consola.

  -> enter_move(board): gestiona el turno del jugador.

  -> make_list_of_free_fields(board): devuelve las coordenadas libres como lista de tuplas.

  -> victory_for(board, sign): comprueba victoria para 'X' o 'O'.

  -> draw_move(board): movimiento aleatorio de la CPU.

  -> playGame(): bucle principal del juego.
