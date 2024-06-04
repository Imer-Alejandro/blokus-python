# main.py

import pygame
import sys
from game import start_game

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

# este modulo del juego se encarga de mostrar la interfaz, simulando elementos como imput de entradas de texto 
# y chebox, para poder definir los nombres de los jugadores en cada partida y el color de sus piezas

# Configuración de la pantalla
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blokus - Python")

# Fuente
font = pygame.font.Font(None, 22)
title_font = pygame.font.Font(None, 64)

# Variables para los campos de texto
player1_name = ''
player2_name = ''
input_box1 = pygame.Rect(WIDTH // 2 - 100, 150, 200, 32)
input_box2 = pygame.Rect(WIDTH // 2 - 100, 300, 200, 32)
color_boxes1 = {color: pygame.Rect(WIDTH // 2 - 115 + i * 50, 220, 32, 32) for i, color in enumerate(COLORS)}
color_boxes2 = {color: pygame.Rect(WIDTH // 2 - 115 + i * 50, 370, 32, 32) for i, color in enumerate(COLORS)}
start_button = pygame.Rect(WIDTH // 2 - 150, 500, 300, 60)
active1 = False
active2 = False
color_selected1 = None
color_selected2 = None

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Bucle principal
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Comprobar si se hace clic en las cajas de texto
            if input_box1.collidepoint(event.pos):
                active1 = not active1
                active2 = False
            elif input_box2.collidepoint(event.pos):
                active2 = not active2
                active1 = False
            else:
                active1 = active2 = False
            
            # Comprobar si se hace clic en los botones de color
            for color, rect in color_boxes1.items():
                if rect.collidepoint(event.pos):
                    color_selected1 = color
            for color, rect in color_boxes2.items():
                if rect.collidepoint(event.pos):
                    color_selected2 = color
            
            # Comprobar si se hace clic en el botón de inicio
            if start_button.collidepoint(event.pos):
                # Verificar que todos los campos están completos
                if player1_name and player2_name and color_selected1 and color_selected2:
                    # Llamar a la función para iniciar el juego
                    start_game(player1_name, color_selected1, player2_name, color_selected2)
                else:
                    print("Por favor complete todos los campos.")
                
        if event.type == pygame.KEYDOWN:
            if active1:
                if event.key == pygame.K_RETURN:
                    active1 = False
                elif event.key == pygame.K_BACKSPACE:
                    player1_name = player1_name[:-1]
                else:
                    player1_name += event.unicode
            elif active2:
                if event.key == pygame.K_RETURN:
                    active2 = False
                elif event.key == pygame.K_BACKSPACE:
                    player2_name = player2_name[:-1]
                else:
                    player2_name += event.unicode
    
    # Dibujar elementos en la pantalla
    draw_text("BLOKUS - Python", title_font, LIGHT_BLUE, screen, WIDTH // 2, 50)
    draw_text("Nombre jugador - 1", font, BLACK, screen, WIDTH // 2, 130)
    draw_text("Color de fichas:", font, BLACK, screen, WIDTH // 2, 200)
    draw_text("Nombre jugador - 2", font, BLACK, screen, WIDTH // 2, 285)
    draw_text("Color de fichas:", font, BLACK, screen, WIDTH // 2, 350)

    # Dibujar campos de texto
    pygame.draw.rect(screen, BLACK, input_box1, 1)
    pygame.draw.rect(screen, BLACK, input_box2, 1)
    
    # Dibujar texto en los campos de texto
    txt_surface1 = font.render(player1_name, True, BLACK)
    screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 10))
    txt_surface2 = font.render(player2_name, True, BLACK)
    screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 10))
    
    # Dibujar botones de color
    for color, rect in color_boxes1.items():
        pygame.draw.rect(screen, COLORS[color], rect)
        if color == color_selected1:
            pygame.draw.rect(screen, (226, 226, 226), rect, 2)
    for color, rect in color_boxes2.items():
        pygame.draw.rect(screen, COLORS[color], rect)
        if color == color_selected2:
            pygame.draw.rect(screen, (226, 226, 226), rect, 2)
    
    # Dibujar botón de inicio
    pygame.draw.rect(screen, LIGHT_BLUE, start_button)
    draw_text("Iniciar partida", font, WHITE, screen, start_button.centerx, start_button.centery)
    
    pygame.display.flip()