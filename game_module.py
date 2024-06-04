
import pygame


# Inicializar pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (57, 106, 238)
COLORS = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128)
}

# # Fuente
font = pygame.font.Font(None, 22)
# title_font = pygame.font.Font(None, 30)

#funcion para dibujar los texto en pantall, possion fuente, color y texto
def draw_text(text, font, color, surface, x, y, center=True):
    text_obj = font.render(text, True, color)
    if center:
        text_rect = text_obj.get_rect(center=(x, y))
    else:
        text_rect = text_obj.get_rect(topleft=(x, y))
    surface.blit(text_obj, text_rect)

#funcion para dibujar las piezas de cada jugador
def draw_pieces(surface, pieces, x, y, color, current_index, move_selected_active):
    piece_y = y
    margin = 10
    for i, (piece_name, (count, cells)) in enumerate(pieces.items()):
        piece_width = max(cell[0] for cell in cells) + 1
        
        alpha = 100 if count > 0 else 255
        if i == current_index and move_selected_active:
            alpha = 255
        for cell in cells:
            cell_rect = pygame.Rect(x + cell[0] * 20, piece_y + cell[1] * 20, 20, 20)
            pygame.draw.rect(surface, color, cell_rect)
            pygame.draw.rect(surface, (255, 255, 255), cell_rect, 1)
            if i == current_index and move_selected_active:
                pygame.draw.rect(surface, (0, 255, 0), cell_rect, 3)
        draw_text(str(count), font, BLACK, surface, x + piece_width * 20 + 20, piece_y + 8, center=False)
        piece_y += (max(cell[1] for cell in cells) + 1) * 25 + margin


#funcion para dibujar la tabla del juego, calculada apartir de la matriz que la conforma
def draw_board(screen, board_state, board_origin, cell_size):
    for row in range(len(board_state)):
        for col in range(len(board_state[row])):
            rect = pygame.Rect(board_origin[0] + col * cell_size, board_origin[1] + row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if board_state[row][col]:
                pygame.draw.rect(screen, board_state[row][col], rect)


