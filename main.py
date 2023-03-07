import numpy as np
import pygame
import sys
import math

NUM_FILAS = 6
NUM_COLUMNAS = 7

# Colores RGB almacenados en variables
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)

pygame.font.init()
FUENTE = pygame.font.SysFont("monospace", 75)


def crear_tablero():
    tablero = np.zeros((NUM_FILAS, NUM_COLUMNAS))
    return tablero


def es_movimiento_valido(tablero, columna):
    return tablero[NUM_FILAS - 1][columna] == 0


def obtener_fila_libre(tablero, columna):
    for fila in range(NUM_FILAS):
        if tablero[fila][columna] == 0:
            return fila


def soltar_ficha(tablero, fila, columna, ficha):
    tablero[fila][columna] = ficha


def imprimir_tablero(tablero):
    print(np.flipud(tablero))


def movimiento_ganador(tablero, ficha):
    # revisando las posiciones horizontales
    for columna in range(NUM_COLUMNAS - 3):
        for fila in range(NUM_FILAS):
            if tablero[fila][columna] == ficha and tablero[fila][columna + 1] == ficha and tablero[fila][
                columna + 2] == ficha and tablero[fila][columna + 3] == ficha:
                return True

    # verificando las posiciones verticales
    for columna in range(NUM_COLUMNAS):
        for fila in range(NUM_FILAS - 3):
            if tablero[fila][columna] == ficha and tablero[fila + 1][columna] == ficha and tablero[fila + 2][
                columna] == ficha and tablero[fila + 3][columna] == ficha:
                return True

    # verificando diagonales positivas
    for columna in range(NUM_COLUMNAS - 3):
        for fila in range(NUM_FILAS - 3):
            if tablero[fila][columna] == ficha and tablero[fila + 1][columna + 1] == ficha and tablero[fila + 2][
                columna + 2] == ficha and tablero[fila + 3][columna + 3] == ficha:
                return True

                # verificando diagonales negativas
    for columna in range(NUM_COLUMNAS - 3):
        for fila in range(3, NUM_FILAS):
            if tablero[fila][columna] == ficha and tablero[fila - 1][columna + 1] == ficha and tablero[fila - 2][
                columna + 2] == ficha and tablero[fila - 3][columna + 3] == ficha:
                return True
def dibujar_tablero(tablero):
    for c in range(NUM_COLUMNAS):
        for r in range(NUM_FILAS):
            pygame.draw.rect(pantalla, AZUL, (c*TAM_CASILLA, r*TAM_CASILLA+TAM_CASILLA, TAM_CASILLA, TAM_CASILLA))
            pygame.draw.circle(pantalla, NEGRO, (int(c*TAM_CASILLA+TAM_CASILLA/2), int(r*TAM_CASILLA+TAM_CASILLA+TAM_CASILLA/2)), RADIO)

    for c in range(NUM_COLUMNAS):
        for r in range(NUM_FILAS):
            if tablero[r][c] == 1:
                pygame.draw.circle(pantalla, AMARILLO, (int(c*TAM_CASILLA+TAM_CASILLA/2), (altura+TAM_CASILLA)-int(r*TAM_CASILLA+TAM_CASILLA+TAM_CASILLA/2)), RADIO)
            elif tablero[r][c] == 2:
                pygame.draw.circle(pantalla, VERDE, (int(c*TAM_CASILLA+TAM_CASILLA/2), (altura+TAM_CASILLA)-int(r*TAM_CASILLA+TAM_CASILLA+TAM_CASILLA/2)), RADIO)

    pygame.display.update()

tablero = crear_tablero()
imprimir_tablero(tablero)
fin_juego = False
turno = 0 # variable para definir usuario 1 y 2

pygame.init()

TAM_CASILLA = 100
ancho = NUM_COLUMNAS * TAM_CASILLA
altura = (NUM_FILAS+1) * TAM_CASILLA

tamanio = (ancho, altura)
RADIO = int(TAM_CASILLA/2 - 5)

pantalla = pygame.display.set_mode(tamanio)
dibujar_tablero(tablero)
pygame.display.update()

while not fin_juego:

    for evento in pygame.event.get():
        # Configurando el cierre de la ventana para que el programa no cierre inesperadamente
        if evento.type == pygame.QUIT:
            sys.exit()

        if evento.type == pygame.MOUSEMOTION:
            pygame.draw.rect(pantalla, NEGRO, (0,0, ancho, TAM_CASILLA))
            posx = evento.pos[0]
            if turno == 0:
                pygame.draw.circle(pantalla, AMARILLO, (posx, int(TAM_CASILLA/2)), RADIO)
            else:
                pygame.draw.circle(pantalla, VERDE, (posx, int(TAM_CASILLA/2)), RADIO)
            pygame.display.update()

        # solicitando la movida al jugador 1
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(pantalla, NEGRO, (0,0, ancho, TAM_CASILLA))
            # print(evento.pos)
            if turno == 0:
                posx = evento.pos[0]
                col = int(math.floor(posx/TAM_CASILLA))
                # col = int(input("Jugador 1 haz tu movida (0,6):"))

                if es_movimiento_valido(tablero, col):
                    fila = obtener_fila_libre(tablero, col)
                    soltar_ficha(tablero, fila, col, 1)

                    if movimiento_ganador(tablero, 1):
                        # print("¡Jugador 1 gana!")
                        etiqueta = FUENTE.render("¡Jugador 1 gana!", 1, AMARILLO)
                        pantalla.blit(etiqueta, (40, 10))
                        fin_juego = True
                # solicitando el movimiento al jugador 2
            else:
                 posx = evento.pos[0]
                 col = int(math.floor(posx / TAM_CASILLA))
                 # columna = int(input("¡Jugador 2, haz tu movimiento (0,6): "))

                 if es_movimiento_valido(tablero, col):
                    fila = obtener_fila_libre(tablero, col)
                    soltar_ficha(tablero, fila, col, 2)

                    if movimiento_ganador(tablero, 2):
                        # print("¡Jugador 2 gana!")
                        etiqueta = FUENTE.render("¡Jugador 2 gana!", 1, VERDE)
                        pantalla.blit(etiqueta, (40, 10))
                        fin_juego = True

            imprimir_tablero(tablero)
            dibujar_tablero(tablero)
            turno += 1  # se incrementa en uno el turno
            turno = turno % 2  # alternando entre cero y uno



            if fin_juego:
                    pygame.time.wait(3000)




