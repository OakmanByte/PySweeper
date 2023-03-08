from enum import Enum

# Enums & Variants
import pygame


class GameState(Enum):
    GAME: str = "Game"
    MENU: str = "MENU"
    EXIT: str = "EXIT"


pygame.init()

# General globals and states
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
GAME_WIDTH = 800  # Width of the game window
GAME_HEIGHT = 800  # Height of the game window
GAME_MARGIN = 50  # Space between the game window and the main window
GAME_X = (WINDOW_WIDTH - GAME_WIDTH) // 2  # X-coordinate of the game window
GAME_Y = (WINDOW_HEIGHT - GAME_HEIGHT) // 2  # Y-coordinate of the game window

# Calculated values
BOARD_DIMENSION = "16x16"
NUM_OF_BOARD_ITEMS = eval(BOARD_DIMENSION.replace("x", "*"))
BOARD_ROWS, BOARD_COLUMNS = map(int, BOARD_DIMENSION.split("x"))
ITEM_SIZE = (GAME_WIDTH // BOARD_ROWS)

# Fonts
FONT_PATH = "fonts/TranscendsGames.otf"
TITLE_FONT = pygame.font.Font(FONT_PATH, 60)
BUTTON_FONT = pygame.font.Font(FONT_PATH, 20)
TIMER_FONT = pygame.font.Font(FONT_PATH, 15)
NUMBER_BOARD_ITEM_FONT = pygame.font.Font(FONT_PATH, 25)

# Colors
BLACK = (0, 0, 0)
SHADOW = (229, 224, 224)
WHITE = (255, 255, 255)
BACKGROUND = (247, 244, 249)
