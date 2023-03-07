import numpy as np
import pygame
import sys
import math
MIN_FILAS = 4
NUM_FILAS = 6 #Definimos las constantes que representan filas
NUM_COLUMNAS = 7 #Definimos las constantes que representan columnas

# Colores RGB almacenados en variables
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)

pygame.font.init() #Inicializamos la fuente de la libreria pygame
FUENTE = pygame.font.SysFont("monospace", 75) #Establecemos la fuente monospace de tamaño 75


def crear_tablero(): #Creamos el tablero
    tablero = np.zeros((NUM_FILAS, NUM_COLUMNAS)) #Utilizamos la libreria numpy para que inicien en 0
    return tablero


def es_movimiento_valido(tablero, columna):
    return tablero[NUM_FILAS - 1][columna] == 0 #Este método es para retornar el tablero con filas = -1 y columna 0


def obtener_fila_libre(tablero, columna): #Acá usamos un ciclo for para recorrer las filas, si la fila y la columna está en 0, retorna el tablero con la fila
    for fila in range(NUM_FILAS):
        if tablero[fila][columna] == 0:
            return fila


def soltar_ficha(tablero, fila, columna, ficha): #Este metodo es para poner las fichas en el tablero
    tablero[fila][columna] = ficha


def imprimir_tablero(tablero): #Este metodo imprime el tablero
    print(np.flipud(tablero))


def movimiento_ganador(tablero, ficha):
    # revisando las posiciones horizontales
    for columna in range(NUM_COLUMNAS - 3):
        for fila in range(NUM_FILAS): #Recorremos columnas y filas, este método es el más importante ya que determina cuando se juntan las 4 fichas en linea
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
        for fila in range(NUM_FILAS - 3): #Aca recorremos otra vez filas y columnas, y determinamos si hay diagonales positivas (hacia la derecha)
            if tablero[fila][columna] == ficha and tablero[fila + 1][columna + 1] == ficha and tablero[fila + 2][
                columna + 2] == ficha and tablero[fila + 3][columna + 3] == ficha:
                return True

    # verificando diagonales negativas
    for columna in range(NUM_COLUMNAS - 3):
        for fila in range(3, NUM_FILAS): #Hacemos lo mismo, pero para ver si hay fichas en diagonales hacia la izquierda
            if tablero[fila][columna] == ficha and tablero[fila - 1][columna + 1] == ficha and tablero[fila - 2][
                columna + 2] == ficha and tablero[fila - 3][columna + 3] == ficha:
                return True
def dibujar_tablero(tablero):
    for c in range(NUM_COLUMNAS):
        for r in range(NUM_FILAS): #Acá dibujamos el tablero con las dos funciones de pygame, para dibujar rectangulos y circulos
            pygame.draw.rect(pantalla, AZUL, (c*TAM_CASILLA, r*TAM_CASILLA+TAM_CASILLA, TAM_CASILLA, TAM_CASILLA))
            pygame.draw.circle(pantalla, NEGRO, (int(c*TAM_CASILLA+TAM_CASILLA/2), int(r*TAM_CASILLA+TAM_CASILLA+TAM_CASILLA/2)), RADIO)

    for c in range(NUM_COLUMNAS): #Recorremos las filas y columnas, y deteminamos los colores de cada jugador, el 1 es color amarillo, el 2 es color verde
        for r in range(NUM_FILAS):
            if tablero[r][c] == 1:
                pygame.draw.circle(pantalla, AMARILLO, (int(c*TAM_CASILLA+TAM_CASILLA/2), (altura+TAM_CASILLA)-int(r*TAM_CASILLA+TAM_CASILLA+TAM_CASILLA/2)), RADIO)
            elif tablero[r][c] == 2:
                pygame.draw.circle(pantalla, VERDE, (int(c*TAM_CASILLA+TAM_CASILLA/2), (altura+TAM_CASILLA)-int(r*TAM_CASILLA+TAM_CASILLA+TAM_CASILLA/2)), RADIO)

    pygame.display.update()  #Esta función es para actualizar el tablero una vez que los jugadores pongan una ficha

tablero = crear_tablero()
imprimir_tablero(tablero)
fin_juego = False #Acá forzamos para que el juego siga
turno = 0 # variable para definir usuario 1 y 2

pygame.init() #Inicializamos la libreria pygame

TAM_CASILLA = 100 #Constante para el tamaño de la casilla
ancho = NUM_COLUMNAS * TAM_CASILLA #Creamos el ancho y el alto multiplicando por el tamaño de cada casilla
altura = (NUM_FILAS+1) * TAM_CASILLA

tamanio = (ancho, altura) #Definimos la variable tamaño y radio para las casillas
RADIO = int(TAM_CASILLA/2 - 5)

pantalla = pygame.display.set_mode(tamanio) #Creamos la variable pantalla, y la definimos con la funcion de pygame para establecer el modo y el tamaño
dibujar_tablero(tablero)
pygame.display.update() #Actualiza el tablero

while not fin_juego: #Cuando fin_juego sea falso, hace esto, (siempre)

    for evento in pygame.event.get(): #Ciclo con la funcion de pygame para obtener el evento
        # Configurando el cierre de la ventana para que el programa no cierre inesperadamente
        if evento.type == pygame.QUIT:
            sys.exit() #Acá usamos la libreria Sys para cerrar la ventana

        if evento.type == pygame.MOUSEMOTION:  #Condicional para dibujar los rectangulos del tablero de color negro
            pygame.draw.rect(pantalla, NEGRO, (0,0, ancho, TAM_CASILLA))
            posx = evento.pos[0]
            if turno == 0: #Forzamos a que inicie el jugador 1 (amarillo)
                pygame.draw.circle(pantalla, AMARILLO, (posx, int(TAM_CASILLA/2)), RADIO)
            else:
                pygame.draw.circle(pantalla, VERDE, (posx, int(TAM_CASILLA/2)), RADIO) #Sigue el turno del jugador verde
            pygame.display.update()

        # solicitando la movida al jugador 1
        if evento.type == pygame.MOUSEBUTTONDOWN: #El movimiento se puede hacer con scroll hacia abajo
            pygame.draw.rect(pantalla, NEGRO, (0,0, ancho, TAM_CASILLA))
            # print(evento.pos)
            if turno == 0:
                posx = evento.pos[0]
                col = int(math.floor(posx/TAM_CASILLA)) #Acá usamos la funcion para el suelo del tablero
                # col = int(input("Jugador 1 haz tu movida (0,6):"))

                if es_movimiento_valido(tablero, col): #Si el movimiento es valido, suelta la ficha en la posicion que esté libre
                    fila = obtener_fila_libre(tablero, col)
                    soltar_ficha(tablero, fila, col, 1)

                    if movimiento_ganador(tablero, 1): #Acá es el evento donde gana el jugador amarillo, y sale el cartel de victoria
                        # print("¡Jugador 1 gana!")
                        etiqueta = FUENTE.render("¡Jugador 1 gana!", 1, AMARILLO)
                        pantalla.blit(etiqueta, (40, 10))
                        fin_juego = True #Forzamos a que termine el juego
                # solicitando el movimiento al jugador 2
            else: # lo mismo con el jugador verde
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

            imprimir_tablero(tablero) #Actualizamos y dibujamos el tablero
            dibujar_tablero(tablero)
            turno += 1  # se incrementa en uno el turno
            turno = turno % 2  # alternando entre cero y uno
            # Variables para llevar un registro de las puntuaciones
            puntuaciones = {
                'AMARILLO': 0,
                'VERDE': 0,
            }
            puntuaciones_triplicadas = {
                'AMARILLO': False,
                'VERDE': False,
            }


def hay_empate(tablero):
    return np.count_nonzero(tablero == 0) == 0 and not movimiento_ganador(tablero,'X') and not movimiento_ganador(tablero, 'O')

def actualizar_puntuaciones(ganador):
    if ganador is None:
        return
    if puntuaciones_triplicadas[ganador]:
       puntuaciones[ganador] *= 3
       puntuaciones_triplicadas[ganador] = False
    else:
       puntuaciones[ganador] += 1
       puntuaciones_triplicadas[ganador] = puntuaciones[ganador] % 2 == 0



    if fin_juego: #Terminamos el juego
                    pygame.time.wait(3000)




