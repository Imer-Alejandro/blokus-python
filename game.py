# game.py

import pygame
import sys
from movimientos import handle_piece_selection, handle_piece_movement, confirm_piece_placement, draw_board_with_piece, draw_transparent_pieces, draw_selection_indicator

# Inicializar pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (57, 106, 238)
COLORS = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128)
}

# Fuente
font = pygame.font.Font(None, 22)
title_font = pygame.font.Font(None, 30)

# Piezas del juego (simplificadas)
player_pieces = {
    "piece1": (6, [(0, 0)]),  # Pieza de 1 bloque con cantidad 6
    "piece2": (7, [(0, 0), (1, 0)]),  # Pieza de 2 bloques con cantidad 7
    "piece3": (8, [(0, 0), (0, 1), (1, 0), (1, 1)]),  # Pieza de 4 bloques
    "piece4": (6, [(0, 0), (0, 1), (0, 2), (1, 2)]),  # Pieza de 4 bloques en L
    "piece5": (4, [(0, 0), (0, 1), (0, 2), (1, 0)]),  # Otra pieza en L
    "piece6": (4, [(0, 0), (0, 1), (1, 1), (1, 2)]),  # Pieza de 4 bloques en Z
    "piece7": (5, [(0, 0), (0, 1), (0, 2), (0, 3)]),  # Pieza de 4 bloques en línea
}

def draw_text(text, font, color, surface, x, y, center=True):
    text_obj = font.render(text, True, color)
    if center:
        text_rect = text_obj.get_rect(center=(x, y))
    else:
        text_rect = text_obj.get_rect(topleft=(x, y))
    surface.blit(text_obj, text_rect)

def draw_pieces(surface, pieces, x, y, color):
    piece_y = y
    margin = 10  # Margen entre piezas
    for piece_name, (count, cells) in pieces.items():
        # Calcular el ancho de la pieza
        piece_width = max(cell[0] for cell in cells) + 1
        # Dibujar la pieza
        for cell in cells:
            cell_rect = pygame.Rect(x + cell[0] * 20, piece_y + cell[1] * 20, 20, 20)
            pygame.draw.rect(surface, color, cell_rect)
            pygame.draw.rect(surface, (255,255,255), cell_rect, 1)
        # Dibujar el número de piezas restantes
        draw_text(str(count), font, BLACK, surface, x + piece_width * 20 + 20, piece_y + 10, center=False)
        piece_y += (max(cell[1] for cell in cells) + 1) * 25 + margin

def start_game(player1_name, player1_color, player2_name, player2_color):
    # Configuración de la pantalla
    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blokus - Python")

    # Tamaño del tablero
    board_size = 20
    cell_size = 30
    board_origin = (WIDTH // 2 - board_size // 2 * cell_size, HEIGHT // 2 - board_size // 2 * cell_size)

    # Inicialización del turno
    current_turn = "player1"
    current_player_color = COLORS[player1_color]
    selected_piece_index = 0
    selected_piece = None
    piece_position = [board_origin[0], board_origin[1]]

    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if selected_piece is None:
                selected_piece_index = handle_piece_selection(event, selected_piece_index, player_pieces)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    selected_piece = list(player_pieces.keys())[selected_piece_index]
                    piece_position = [board_origin[0], board_origin[1]]
            else:
                piece_position = handle_piece_movement(event, piece_position)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if player_pieces[selected_piece][0] > 0:
                        player_pieces[selected_piece] = (player_pieces[selected_piece][0] - 1, player_pieces[selected_piece][1])
                        current_turn = "player2" if current_turn == "player1" else "player1"
                        current_player_color = COLORS[player2_color] if current_turn == "player2" else COLORS[player1_color]
                        selected_piece = None
        
        # Dibujar el título del juego
        draw_text("BLOKUS - Python", title_font, LIGHT_BLUE, screen, WIDTH // 2, 10)
        
        # Dibujar el indicador de turno
        draw_text(f"Turno de: {player1_name if current_turn == 'player1' else player2_name}", font, BLACK, screen, WIDTH // 2, 30)

        # Dibujar nombres de los jugadores
        draw_text(player1_name, font, COLORS[player1_color], screen, 100, 150)
        draw_text(player2_name, font, COLORS[player2_color], screen, 900, 150)
        
        # Dibujar piezas de los jugadores
        draw_pieces(screen, player_pieces, 50, 200, COLORS[player1_color])
        draw_pieces(screen, player_pieces, 850, 200, COLORS[player2_color])

        # Dibujar el indicador de selección de piezas
        draw_selection_indicator(screen, player_pieces, selected_piece_index, 50 if current_turn == "player1" else 850, 200, COLORS[player1_color] if current_turn == "player1" else COLORS[player2_color])
        
        # Dibujar el tablero y la pieza seleccionada
        if selected_piece is not None:
            draw_board_with_piece(screen, board_origin, board_size, cell_size, player_pieces[selected_piece][1], piece_position, current_player_color)
        
        pygame.display.flip()


