import itertools
import random

import pygame
from pygame import Surface
from pygame.event import Event

from GameTimer import timer
from classes import Bomb, Number, BoardItemTypes
from globals import WINDOW_WIDTH, GameState, GAME_X, GAME_Y, BLACK, TIMER_FONT, board_rows, board_columns, \
    number_of_board_items, item_size
from death_screen import DeathScreen
from win_screen import WinScreen
from state_machine import state
from screen import Screen


class Game(Screen):
    window: Surface
    __board: list = None
    number_of_bombs: int = 1
    completion_time: str

    def __init__(self, window: Surface):
        timer.start_timer()
        if self.number_of_bombs > number_of_board_items:
            raise ValueError(f"You can't have more bombs than number of board squares:"
                             f" {self.number_of_bombs} > {number_of_board_items} ")
        self.window = window
        self.setup()

    def setup(self):
        self.populate_board_array(self.number_of_bombs)
        self.set_board_item_locations()

    def render(self, event: Event):
        self.render_boarder()
        self.render_timer()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            # left and right mouse click respectively
            if mouse_presses[0] | mouse_presses[2]:
                mouse_pos = pygame.mouse.get_pos()
                for board_item in self.__board:
                    if board_item.is_over(mouse_pos):
                        if mouse_presses[0]:
                            board_item.reveal()
                            if board_item.type == BoardItemTypes.NUMBER:
                                self.check_win_condition()
                            else:
                                state.set_screen(DeathScreen(self.window))
                        else:
                            board_item.set_flag()

        for board_item in self.__board:
            board_item.draw(self.window, outline=True)

    def populate_board_array(self, number_of_bombs: int):
        # Generate randomized locations for the bombs
        bomb_locations: list[tuple[int, int]] = list(
            random.sample([(i, j) for i in range(board_rows) for j in range(board_columns)], number_of_bombs))

        board: list[list[Number | Bomb]] = [[Number() for _ in range(board_rows)] for _ in range(board_columns)]

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
        for row in range(board_rows):
            for column in range(board_columns):
                if board[row][column].type == BoardItemTypes.NUMBER:
                    board[row][column].bomb_count = sum(
                        board[row + r][column + c].type == BoardItemTypes.BOMB for r, c in neighbour_indices if
                        0 <= row + r < board_rows and 0 <= column + c < board_columns
                    )

        # Flatten the list of lists into a single list
        flat_board_items = list(itertools.chain(*board))

        self.__board = flat_board_items

    def set_board_item_locations(self):
        for i in range(number_of_board_items):
            row = i // board_rows
            col = i % board_columns
            x = (col * item_size) + GAME_X
            y = (row * item_size) + GAME_Y
            self.__board[i].set_pos(x=x, y=y)

    def render_boarder(self):
        pygame.draw.rect(self.window, BLACK, self.window.get_rect(), 2)

    def render_timer(self):
        timer_text = TIMER_FONT.render(timer.get_elapsed_time_str_formatted(), True, (50, 0, 0))
        self.window.blit(timer_text, (WINDOW_WIDTH - timer_text.get_width() - 10, 10))

    # TODO: Better way?
    def reset_board(self):
        self.setup()

    def check_win_condition(self):
        for board_item in self.__board:
            if board_item.type == BoardItemTypes.NUMBER and board_item.hidden:
                return False

        state.set_screen(WinScreen(self.window, timer.get_elapsed_time_str_formatted()))
