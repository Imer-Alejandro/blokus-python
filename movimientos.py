#funciones de validacion de moviminetos, turnos y renderizado del estado de la partida en el tablero y el valor de 
#la ficha en el tablero y sus contadores durante la partida 

import pygame

# funcion para navegar por las piezas del jugador en turno y ver de forma interactiva cual se va selecionar
def navigate_and_select_piece(current_index, pieces,state_active):
    if state_active:
        keys = pygame.key.get_pressed()
        #logica para moverse por las piezas del jugador en turno hasta selecionar una
        if keys[pygame.K_UP]:
            current_index = (current_index - 1) % len(pieces)
        elif keys[pygame.K_DOWN]:
            current_index = (current_index + 1) % len(pieces)
    #retorna la referencia del indice de la prieza en la que esta segun se navega, asi se aplica el borde verde 
    # que indica en que pieza se encuentra el seclector
    return current_index

# funcion para dibujar en el tablero la pieza selecionada luego de confirmarla
def draw_selected_piece(surface, current_index, pieces, piece_x, piece_y, cell_size, board_origin, player_color):
    if current_index is not None:
        piece_name = list(pieces.keys())[current_index]
        _, cells = pieces[piece_name]
        # Dibujar la ficha selecionada en el tablero tomando la referencia del indice de esta
        for cell in cells:
            cell_rect = pygame.Rect(board_origin[0] + (piece_x + cell[0]) * cell_size,
                                    board_origin[1] + (piece_y + cell[1]) * cell_size,
                                    cell_size, cell_size)
            pygame.draw.rect(surface, player_color, cell_rect)
            pygame.draw.rect(surface, (0, 0, 0), cell_rect, 1)


#funcion para validar si se puede colocar la pieza en una posision determinada dentro del tablero
def can_place_piece(board_state, piece, pos_x, pos_y, board_size):
    for cell in piece:
        x, y = cell[0] + pos_x, cell[1] + pos_y
        # se valida que la antes de fijar la posision de la pieza este dentro de los limites del tablero
        if x < 0 or x >= board_size or y < 0 or y >= board_size:
            return False
        if board_state[y][x] is not None:
            return False
    return True

#funcion para pocicionar la pieza a dibujar dentro del tablero antes de fijarla y luego de selecionarla
def place_piece(board_state, piece, pos_x, pos_y, color):
    for cell in piece:
        x, y = cell[0] + pos_x, cell[1] + pos_y
        board_state[y][x] = color