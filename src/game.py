import itertools
from dataclasses import dataclass

import pygame

from classes import Bomb, Number, BoardItemTypes
import random

# Initialize all the Pygame modules and prepare them for use
from constants import WINDOW_WIDTH, BOARD_ROWS, BOARD_COLUMNS, NUM_OF_BOARD_ITEMS, ITEM_SIZE, \
    ITEM_SPACING, timer_font, GameState, SCREEN, SCREEN
from state_machine import state

start_time = pygame.time.get_ticks()


@dataclass
class Game:
    frame: pygame.Rect = None
    board: list = None

    def __post_init__(self):
        self.board = self.populate_board_array()
        self.set_board_item_locations()

    def run(self):
        # Get the current time in seconds
        current_time_formatted = f"Time: {(pygame.time.get_ticks() - start_time) // 1000}s"
        # Render the timer text and blit it to the top right corner of the screen
        timer_text = timer_font.render(current_time_formatted, True, (50, 0, 0))
        SCREEN.blit(timer_text, (WINDOW_WIDTH - timer_text.get_width() - 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.set_state(GameState.EXIT)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                # left and right mouse click respectively
                if mouse_presses[0] | mouse_presses[2]:
                    mouse_pos = pygame.mouse.get_pos()
                    for board_item in self.board:
                        if board_item.is_over(mouse_pos):
                            if mouse_presses[0]:
                                board_item.reveal()
                            else:
                                board_item.set_flag()

        for board_item in self.board:
            board_item.draw(SCREEN, outline=True)

    @staticmethod
    def populate_board_array(number_of_bombs: int = 40):
        # Generate randomized locations for the bombs
        bomb_locations: list[tuple[int, int]] = [(x, y) for x, y in
                                                 random.sample(
                                                     [(i, j) for i in range(BOARD_ROWS) for j in range(BOARD_COLUMNS)],
                                                     number_of_bombs)]

        board: list[list[Number | Bomb]] = [[Number() for _ in range(BOARD_ROWS)] for _ in range(BOARD_COLUMNS)]

        # Populate with Bombs
        for bomb_location in bomb_locations:
            board[bomb_location[0]][bomb_location[1]] = Bomb()

        # Calculate neighbouring bombs for each number item
        '''
        Consider location = [R][C]. Then the 8 neighbours are:
        [R-1][C]
        [R+1][C]
        [R][C-1]
        [R][C+1]
        [R-1][C-1]
        [R-1][C+1]
        [R+1][C-1]
        [R+1][C+1]
        '''
        neighbour_indices = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]
        for row in range(BOARD_ROWS):
            for column in range(BOARD_COLUMNS):
                if board[row][column].type == BoardItemTypes.NUMBER:
                    board[row][column].bomb_count = sum(
                        board[row + r][column + c].type == BoardItemTypes.BOMB for r, c in neighbour_indices if
                        0 <= row + r < BOARD_ROWS and 0 <= column + c < BOARD_COLUMNS
                    )

        # Flatten the list of lists into a single list
        flat_board_items = list(itertools.chain(*board))

        return flat_board_items

    def set_board_item_locations(self):
        for i in range(NUM_OF_BOARD_ITEMS):
            row = i // BOARD_ROWS
            col = i % BOARD_COLUMNS
            x = (col * ITEM_SIZE) + ITEM_SPACING
            y = (row * ITEM_SIZE) + ITEM_SPACING
            self.board[i].set_pos(x=x, y=y)
