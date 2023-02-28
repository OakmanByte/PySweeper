import pygame

from button import Button, Bomb
import random

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()


def main():
    pygame.init()
    SCREEN.fill((0, 0, 0))

    while True:
        game_board = init_board()
        print(game_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    print("Left Mouse key was clicked")
                    mouse_position = pygame.mouse.get_pos()

        pygame.display.update()


def init_board(rows: int = 8, columns: int = 8, button_size: int = 20, spacing: int = 5, number_of_bombs: int = 5):

    # Generate random location for bombs
    entity_list = [int]
    for i in range(0, number_of_bombs):
        n = random.randint(0, rows * columns)
        entity_list.append(n)

    # Populate board with bombs and normal squares
    board = []
    for row in range(rows):
        game_row = []
        for column in range(columns):
            if (row + column) in entity_list:
                game_row.append(Bomb(x + spacing, y + spacing, button_size, button_size))
            else:
                game_row.append(Button(x + spacing, y + spacing, button_size, button_size, (129, 0, 128)))
        board.append(game_row)

    return board
    '''
    button_grid = []
    for x in range(spacing, WINDOW_WIDTH, button_size + spacing):
        row = []
        for y in range(spacing, WINDOW_HEIGHT, button_size + spacing):
            button = Button(x, y, button_size, button_size, (129, 0, 128))
            row.append(button)
        button_grid.append(row)
    return button_grid
    '''


if __name__ == '__main__':
    main()
