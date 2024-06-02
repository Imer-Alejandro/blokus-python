import pygame

def navigate_and_select_piece(current_index, pieces):
    keys = pygame.key.get_pressed()  # Obtener el estado de las teclas

    if keys[pygame.K_UP]:  # Si se presiona la tecla arriba
        current_index = (current_index - 1) % len(pieces)  # Seleccionar la pieza anterior
    elif keys[pygame.K_DOWN]:  # Si se presiona la tecla abajo
        current_index = (current_index + 1) % len(pieces)  # Seleccionar la pieza siguiente
    elif keys[pygame.K_SPACE]:  # Si se presiona la tecla de espacio
        # Lógica para validar y seleccionar la pieza
        piece_name = list(pieces.keys())[current_index]
        count, _ = pieces[piece_name]
        if count > 0:
            pieces[piece_name] = (count - 1, pieces[piece_name][1])  # Decrementar el contador de la pieza seleccionada

    return current_index
