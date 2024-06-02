#funciones de validacion de moviminetos, turnos y renderizado del estado de la partida en el tablero y el valor de 
#la ficha en el tablero y sus contadores durante la partida 

import pygame

def navigate_and_select_piece(current_index, pieces):
    keys = pygame.key.get_pressed()  # Obtener el estado de las teclas

    if keys[pygame.K_UP]:  # Si se presiona la tecla arriba
        current_index = (current_index - 1) % len(pieces)  # Seleccionar la pieza anterior
    elif keys[pygame.K_DOWN]:  # Si se presiona la tecla abajo
        current_index = (current_index + 1) % len(pieces)  # Seleccionar la pieza siguiente

    return current_index