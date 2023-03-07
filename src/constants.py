from enum import Enum


class GameState(Enum):
    GAME: str = "Game"
    MENU: str = "MENU"
    EXIT: str = "EXIT"


# General globals and states
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900

GAME_WIDTH = 800  # Width of the game window
GAME_HEIGHT = 800  # Height of the game window
GAME_MARGIN = 50  # Space between the game window and the main window
GAME_X = (WINDOW_WIDTH - GAME_WIDTH) // 2  # X-coordinate of the game window
GAME_Y = (WINDOW_HEIGHT - GAME_HEIGHT) // 2  # Y-coordinate of the game window

BOARD_DIMENSION = "16x16"
NUM_OF_BOARD_ITEMS = eval(BOARD_DIMENSION.replace("x", "*"))
BOARD_ROWS, BOARD_COLUMNS = map(int, BOARD_DIMENSION.split("x"))
ITEM_SIZE = (GAME_WIDTH // BOARD_ROWS)
