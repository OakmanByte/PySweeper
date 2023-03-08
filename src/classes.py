from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import pygame
from pygame.font import Font

from constants import ITEM_SIZE, GameState, BLACK, WHITE, BUTTON_FONT, NUMBER_BOARD_ITEM_FONT
from state_machine import state


class BoardItemTypes(Enum):
    BOMB = "Bomb"
    NUMBER = "Number"


@dataclass
class TextButton:
    x: int
    y: int
    button_text: str
    font: Font = BUTTON_FONT
    width: int = 150
    height: int = 100
    color: Tuple[int, int, int] | str = WHITE

    def draw(self, surface: pygame.Surface):
        # Define the button rectangle
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Draw the button
        pygame.draw.rect(surface, self.color, button_rect, border_radius=20)

        # Draw the button text
        if self.button_text:
            button_text_surface = self.font.render(self.button_text, True, pygame.Color('black'))
            text_x = button_rect.x + (button_rect.width - button_text_surface.get_width()) // 2
            text_y = button_rect.y + (button_rect.height - button_text_surface.get_height()) // 2
            surface.blit(button_text_surface, (text_x, text_y))

    def is_over(self, mouse_position: Tuple[int, int]) -> bool:
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return button_rect.collidepoint(mouse_position)


@dataclass
class BoardItem:
    type: BoardItemTypes
    hidden: bool = True
    x: int = 0
    y: int = 0
    size: int = ITEM_SIZE
    color: Tuple[int, int, int] | str = WHITE
    flagged: bool = False

    def is_over(self, mouse_position: tuple[int, int]) -> bool:
        button_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return button_rect.collidepoint(mouse_position)

    def draw(self, screen, outline: bool = False):
        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.size, self.size))
        if outline:
            pygame.draw.rect(screen, color=BLACK, rect=(self.x, self.y, self.size, self.size), width=1)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_dimensions(self, height, width):
        self.size = height
        self.size = width

    def reveal(self):
        self.hidden = False

    def set_flag(self):
        self.flagged = not self.flagged


@dataclass
class Bomb(BoardItem):
    type: BoardItemTypes = BoardItemTypes.BOMB

    def draw(self, screen, outline: bool = False):
        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.size, self.size))
        if outline:
            pygame.draw.rect(screen, color=BLACK, rect=(self.x, self.y, self.size, self.size), width=1)
        if self.flagged:
            # Load the image
            image = pygame.image.load('box.svg')

            # Draw the image onto the screen
            screen.blit(image, (self.x + self.size / 2, self.y + self.size / 2))

    def reveal(self):
        self.hidden = False
        self.color = "red"
        state.set_state(GameState.MENU)


@dataclass
class Number(BoardItem):
    type: BoardItemTypes = BoardItemTypes.NUMBER
    bomb_count: int = 5
    font: Font = NUMBER_BOARD_ITEM_FONT

    def draw(self, screen, outline: bool = False):

        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.size, self.size))
        if outline:
            pygame.draw.rect(screen, color=BLACK, rect=(self.x, self.y, self.size, self.size), width=1)
        if not self.hidden:
            img = self.font.render(str(self.bomb_count), True, BLACK)
            # TODO: Location of number to be right in middle
            screen.blit(img, (self.x + self.size / 2, self.y + self.size - self.font.get_height()))

    def reveal(self):
        self.hidden = False
        self.color = "green"
