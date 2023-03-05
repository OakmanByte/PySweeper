from enum import Enum

import pygame


class GameState(Enum):
    GAME: str = "Game"
    MENU: str = "MENU"
    EXIT: str = "EXIT"


# General globals and states
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
BOARD_HEIGHT = 700
BOARD_WIDTH = 700
BOARD_DIMENSION = "16x16"
NUM_OF_BOARD_ITEMS = eval(BOARD_DIMENSION.replace("x", "*"))
BOARD_ROWS, BOARD_COLUMNS = map(int, BOARD_DIMENSION.split("x"))
ITEM_SPACING = 5
ITEM_SIZE = (BOARD_WIDTH // BOARD_ROWS) - ITEM_SPACING

# Pygame settings
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('PySweeper v0.1')

# Fonts
timer_font = pygame.font.SysFont("arial", 20)
