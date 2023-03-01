import math

import pygame

from button import Button
import random

WINDOW_HEIGHT = 614
WINDOW_WIDTH = 614
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
BOARD_HEIGHT = 512
BOARD_WIDTH = 512
NUM_OF_BOARD_ITEMS = 64
OFFSET = round((WINDOW_WIDTH / 2) - (BOARD_WIDTH / 2))
FRAME_BORDER_COLOR = (128, 128, 128)
FRAME_BORDER_THICKNESS = 4


def main():
    pygame.init()
    SCREEN.fill((0, 0, 0))
    game_board = populate_board_array()
    set_board_item_locations(game_board)
    print(game_board)

    while True:
        for event in pygame.event.get():

            pygame.draw.rect(SCREEN,
                             color=FRAME_BORDER_COLOR,
                             rect=(
                                 OFFSET, OFFSET, BOARD_WIDTH + (FRAME_BORDER_THICKNESS * 2),
                                 BOARD_HEIGHT + (FRAME_BORDER_THICKNESS * 2)),
                             width=4)

            for board_item in game_board:
                board_item.draw(SCREEN, outline=True)
                if board_item.is_over(pygame.mouse.get_pos()):
                    print("over a button")

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    print("Left Mouse key was clicked")

        pygame.display.update()


def populate_board_array(number_of_bombs: int = 5):
    # Generate random location for bombs
    entity_list = [int]
    for i in range(0, number_of_bombs):
        n = random.randint(0, NUM_OF_BOARD_ITEMS)
        entity_list.append(n)

    # Populate board with bombs and normal squares
    board = []
    for row in range(NUM_OF_BOARD_ITEMS):
        if row in entity_list:
            board.append(Button(color=(255, 0, 0)))
        else:
            board.append(Button(color=(255, 255, 255)))

    return board


def set_board_item_locations(game_board: list[Button]):
    spacing = 5
    size = BOARD_HEIGHT // math.sqrt(NUM_OF_BOARD_ITEMS)
    for i in range(NUM_OF_BOARD_ITEMS):
        row = i // 8
        col = i % 8
        x = (col * size) + spacing
        y = (row * size) + spacing
        game_board[i].set_pos(x=x + OFFSET, y=y + OFFSET)


if __name__ == '__main__':
    main()
