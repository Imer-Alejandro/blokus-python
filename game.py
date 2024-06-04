import pygame
import sys
from movimientos import draw_selected_piece

# Inicializar pygame
pygame.init()

#el juego va cambiando los turnos de los jugadores, el funcionamiento es el de navegar por las piezas de un jugador
# en turno luego presionar la tecla de espacio para selecionarla esta apace en el tablero se puede mover y al presionar
# enter en se quedara fija en la posicion indicada, el contador de cantida de esa pieza se descontara en uno cada vez que se 
# selecione, no se pueden selecionar fichas que tengan un contador en 0, y no se pueden colocar piezas en el tablero en 
# pociciones donde no estan libres todos los espacios que esta ocupa

# solo la primera jugada puede colocarse en cualquier lugar, el resto de jugadas deberan ir tocando una pieza de las misma 
# que ella osea del mismo color y del mismo jugador

# la partida termina cuando uno de los jugadores coloque todas sus piezas en el tablero, si un jugador se  queda sin lugares
# praa colocar sus gichas el turno de este pasa al siguiente jjugador

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

# Fuente
font = pygame.font.Font(None, 22)
title_font = pygame.font.Font(None, 30)

# Estado de piezas de cada jugador para tener su forma y contador
player_pieces = {
    "player1": {
        "piece1": (6, [(0, 0)]),
        "piece2": (7, [(0, 0), (1, 0)]),
        "piece3": (8, [(0, 0), (0, 1), (1, 0), (1, 1)]),
        "piece4": (6, [(0, 0), (0, 1), (0, 2), (1, 2)]),
        "piece5": (4, [(0, 0), (0, 1), (0, 2), (1, 0)]),
        "piece6": (4, [(0, 0), (0, 1), (1, 1), (1, 2)]),
        "piece7": (5, [(0, 0), (0, 1), (0, 2), (0, 3)]),
    },
    "player2": {
        "piece1": (6, [(0, 0)]),
        "piece2": (7, [(0, 0), (1, 0)]),
        "piece3": (8, [(0, 0), (0, 1), (1, 0), (1, 1)]),
        "piece4": (6, [(0, 0), (0, 1), (0, 2), (1, 2)]),
        "piece5": (4, [(0, 0), (0, 1), (0, 2), (1, 0)]),
        "piece6": (4, [(0, 0), (0, 1), (1, 1), (1, 2)]),
        "piece7": (5, [(0, 0), (0, 1), (0, 2), (0, 3)]),
    }
}

# Función para dibujar los textos en pantalla 
def draw_text(text, font, color, surface, x, y, center=True):
    text_obj = font.render(text, True, color)
    if center:
        text_rect = text_obj.get_rect(center=(x, y))
    else:
        text_rect = text_obj.get_rect(topleft=(x, y))
    surface.blit(text_obj, text_rect)

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

def draw_board(screen, board_state, board_origin, cell_size):
    for row in range(len(board_state)):
        for col in range(len(board_state[row])):
            rect = pygame.Rect(board_origin[0] + col * cell_size, board_origin[1] + row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if board_state[row][col]:
                pygame.draw.rect(screen, board_state[row][col], rect)

def can_place_piece(board_state, piece, pos_x, pos_y, board_size):
    for cell in piece:
        x, y = cell[0] + pos_x, cell[1] + pos_y
        if x < 0 or x >= board_size or y < 0 or y >= board_size:
            return False
        if board_state[y][x] is not None:
            return False
    return True

def place_piece(board_state, piece, pos_x, pos_y, color):
    for cell in piece:
        x, y = cell[0] + pos_x, cell[1] + pos_y
        board_state[y][x] = color

def start_game(player1_name, player1_color, player2_name, player2_color):
    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blokus - Python")

    board_size = 20
    cell_size = 30
    board_origin = [WIDTH // 2 - board_size // 2 * cell_size, HEIGHT // 2 - board_size // 2 * cell_size]

    board_state = [[None for _ in range(board_size)] for _ in range(board_size)]

    current_turn = "player1"

    selected_piece_index = 0
    selected = False
    move_selected_active = True
    piece_x, piece_y = 0, 0

    running = True
    while running:
        screen.fill(WHITE)
        draw_board(screen, board_state, board_origin, cell_size)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if move_selected_active:
                        piece_name = list(player_pieces[current_turn].keys())[selected_piece_index]
                        count, piece = player_pieces[current_turn][piece_name]
                        if count > 0:
                            player_pieces[current_turn][piece_name] = (count - 1, piece)
                            selected = True
                            move_selected_active = False
                    else:
                        move_selected_active = True

                elif event.key == pygame.K_RETURN and selected:
                    piece_name = list(player_pieces[current_turn].keys())[selected_piece_index]
                    piece = player_pieces[current_turn][piece_name][1]
                    if can_place_piece(board_state, piece, piece_x, piece_y, board_size):
                        place_piece(board_state, piece, piece_x, piece_y, COLORS[player1_color if current_turn == "player1" else player2_color])
                        current_turn = "player2" if current_turn == "player1" else "player1"
                        selected = False
                        selected_piece_index = 0
                        move_selected_active = True

                elif event.key == pygame.K_UP:
                    if selected:
                        if piece_y > 0:
                            piece_y -= 1
                    elif move_selected_active:
                        selected_piece_index = (selected_piece_index - 1) % len(player_pieces[current_turn])
                elif event.key == pygame.K_DOWN:
                    if selected:
                        if piece_y < board_size - 1:
                            piece_y += 1
                    elif move_selected_active:
                        selected_piece_index = (selected_piece_index + 1) % len(player_pieces[current_turn])
                elif event.key == pygame.K_LEFT:
                    if selected and piece_x > 0:
                        piece_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if selected and piece_x < board_size - 1:
                        piece_x += 1

        pygame.time.Clock().tick(10)

        draw_text("BLOKUS - Python", title_font, LIGHT_BLUE, screen, WIDTH // 2, 10)
        
        draw_text(f"Turno de: {player1_name if current_turn == 'player1' else player2_name}", font, BLACK, screen, WIDTH // 2, 30)
       
        draw_text(player1_name, font, COLORS[player1_color], screen, 120, 140)
        draw_text(player2_name, font, COLORS[player2_color], screen, 920, 140)

        if current_turn == 'player1':
            draw_pieces(screen, player_pieces["player1"], 50, 200, COLORS[player1_color], selected_piece_index, move_selected_active)
            draw_pieces(screen, player_pieces["player2"], 850, 200, COLORS[player2_color], selected_piece_index, False)
        else:
            draw_pieces(screen, player_pieces["player2"], 850, 200, COLORS[player2_color], selected_piece_index, move_selected_active)
            draw_pieces(screen, player_pieces["player1"], 50, 200, COLORS[player1_color], selected_piece_index, False)
        
        if selected:
            draw_selected_piece(screen, selected_piece_index, player_pieces[current_turn], piece_x, piece_y, cell_size, board_origin, COLORS[player1_color if current_turn == "player1" else player2_color])

        pygame.display.update()