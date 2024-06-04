#funciones de validacion de moviminetos, turnos y renderizado del estado de la partida en el tablero y el valor de 
#la ficha en el tablero y sus contadores durante la partida 

import pygame
def navigate_and_select_piece(current_index, pieces,state_active):
    if state_active:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            current_index = (current_index - 1) % len(pieces)
        elif keys[pygame.K_DOWN]:
            current_index = (current_index + 1) % len(pieces)

    return current_index

def draw_selected_piece(surface, current_index, pieces, piece_x, piece_y, cell_size, board_origin, player_color):
    if current_index is not None:
        piece_name = list(pieces.keys())[current_index]
        _, cells = pieces[piece_name]

        # Dibujar la pieza en el tablero
        for cell in cells:
            cell_rect = pygame.Rect(board_origin[0] + (piece_x + cell[0]) * cell_size,
                                    board_origin[1] + (piece_y + cell[1]) * cell_size,
                                    cell_size, cell_size)
            pygame.draw.rect(surface, player_color, cell_rect)
            pygame.draw.rect(surface, (0, 0, 0), cell_rect, 1)