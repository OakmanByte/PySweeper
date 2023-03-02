import itertools
import math

import pygame

from button import Bomb, Number
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
pygame.display.set_caption('PySweeper v0.1')


def main():
    pygame.init()
    SCREEN.fill((0, 0, 0))
    game_board = populate_board_array()
    set_board_item_locations(game_board)
    is_running = True

    while is_running:
        for event in pygame.event.get():

            pygame.draw.rect(SCREEN,
                             color=FRAME_BORDER_COLOR,
                             rect=(
                                 OFFSET, OFFSET, BOARD_WIDTH + (FRAME_BORDER_THICKNESS * 2),
                                 BOARD_HEIGHT + (FRAME_BORDER_THICKNESS * 2)),
                             width=4)

            for board_item in game_board:
                board_item.draw(SCREEN, outline=True)

            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    for board_item in game_board:
                        if board_item.is_over(mouse_pos):
                            board_item.reveal()
                            # print("Game over")
                            # is_running = False  # Set isRunning to False when game over

        pygame.display.update()

    pygame.quit()  # Quit Pygame outside the loop


def populate_board_array(number_of_bombs: int = 5):
    bomb_locations: list[tuple[int, int]] = [(x, y) for x, y in
                                             random.sample([(i, j) for i in range(8) for j in range(8)],
                                                           number_of_bombs)]

    board: list[list[Number | Bomb]] = [[Number() for _ in range(8)] for _ in range(8)]

    # Calculate neighbouring bombs for each number item
    # TODO

    for bomb_location in bomb_locations:
        board[bomb_location[0]][bomb_location[1]] = Bomb()

    # Flatten the list of lists into a single list
    flat_board_items = list(itertools.chain(*board))

    return flat_board_items


def set_board_item_locations(game_board):
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
