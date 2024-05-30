# movimientos.py

import pygame

def draw_transparent_pieces(screen, piece_cells, position, color, opacity=128):
    for cell in piece_cells:
        cell_rect = pygame.Rect(position[0] + cell[0] * 30, position[1] + cell[1] * 30, 30, 30)
        pygame.draw.rect(screen, (*color, opacity), cell_rect)
        pygame.draw.rect(screen, (0, 0, 0, opacity), cell_rect, 1)

def draw_highlighted_piece(screen, cells, x, y, color):
    for cell in cells:
        cell_rect = pygame.Rect(x + cell[0] * 20, y + cell[1] * 20, 20, 20)
        pygame.draw.rect(screen, color, cell_rect)
        pygame.draw.rect(screen, (255, 255, 255), cell_rect, 1)

def handle_piece_selection(event, selected_piece_index, player_pieces):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            selected_piece_index = (selected_piece_index + 1) % len(player_pieces)
        elif event.key == pygame.K_UP:
            selected_piece_index = (selected_piece_index - 1) % len(player_pieces)
        elif event.key == pygame.K_SPACE:
            return selected_piece_index
    return selected_piece_index

def handle_piece_movement(event, piece_position):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            piece_position[0] -= 30
        elif event.key == pygame.K_RIGHT:
            piece_position[0] += 30
        elif event.key == pygame.K_UP:
            piece_position[1] -= 30
        elif event.key == pygame.K_DOWN:
            piece_position[1] += 30
    return piece_position

def confirm_piece_placement(event, selected_piece, player_pieces, current_turn):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        if player_pieces[selected_piece][0] > 0:
            player_pieces[selected_piece] = (player_pieces[selected_piece][0] - 1, player_pieces[selected_piece][1])
            current_turn = "player2" if current_turn == "player1" else "player1"
    return current_turn

def draw_board_with_piece(screen, board_origin, board_size, cell_size, piece_cells, piece_position, color):
    for row in range(board_size):
        for col in range(board_size):
            rect = pygame.Rect(board_origin[0] + col * cell_size, board_origin[1] + row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
    draw_transparent_pieces(screen, piece_cells, piece_position, color)

def draw_selection_indicator(screen, pieces, selected_piece_index, x, y, color):
    piece_y = y
    margin = 10  # Margen entre piezas
    index = 0
    for piece_name, (count, cells) in pieces.items():
        if index == selected_piece_index:
            draw_highlighted_piece(screen, cells, x, piece_y, (255, 0, 0))  # Resaltar la pieza seleccionada
        else:
            draw_highlighted_piece(screen, cells, x, piece_y, color)
        piece_y += (max(cell[1] for cell in cells) + 1) * 25 + margin
        index += 1
