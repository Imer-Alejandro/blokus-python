# game.py

import pygame
import sys

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

#name game 


# Fuente
font = pygame.font.Font(None, 22)
title_font = pygame.font.Font(None, 64)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def start_game(player1_name, player1_color, player2_name, player2_color):
    # Configuración de la pantalla
    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blokus - Python")

    # Tamaño del tablero
    board_size = 20
    cell_size = 30
    board_origin = (WIDTH // 2 - board_size // 2 * cell_size, HEIGHT // 2 - board_size // 2 * cell_size)

    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Dibujar nombres de los jugadores
        draw_text(player1_name, font, COLORS[player1_color], screen, 70, 50)
        draw_text(player2_name, font, COLORS[player2_color], screen, 900, 50)
        
        # Dibujar el tablero
        for row in range(board_size):
            for col in range(board_size):
                rect = pygame.Rect(board_origin[0] + col * cell_size, board_origin[1] + row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, BLACK, rect, 1)
        
        pygame.display.flip()
