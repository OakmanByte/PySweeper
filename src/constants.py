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


# Set up the window dimensions
window_width = 800
window_height = 600

# Set up the main game screen dimensions
game_width = 600
game_height = 400

# Set up the outer screen dimensions
outer_width = window_width - game_width
outer_height = window_height

# Create the window and the main game screen surface
window = pygame.display.set_mode((window_width, window_height))
game_surface = pygame.Surface((game_width, game_height))

# Create the outer screen surface
outer_surface = pygame.Surface((outer_width, outer_height))

# Set the background color of the outer screen surface
outer_surface.fill((255, 255, 255))

# Set up the position of the game screen within the window
game_x = (window_width - game_width) // 2
game_y = (window_height - game_height) // 2

# Set up the position of the outer screen within the window
outer_x = 0
outer_y = 0

# Blit the game surface onto the window at the game position
window.blit(game_surface, (game_x, game_y))

# Blit the outer surface onto the window at the outer position
window.blit(outer_surface, (outer_x, outer_y))