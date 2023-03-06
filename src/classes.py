from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import pygame

from constants import ITEM_SIZE, GameState
from state_machine import state


class BoardItemTypes(Enum):
    BOMB = "Bomb"
    NUMBER = "Number"


@dataclass
class MenuButton:
    x: int = 0
    y: int = 0
    width: int = 100
    height: int = 50
    color: Tuple[int, int, int] | str = (255, 255, 255)
    button_text: str | None = None

    def draw(self, surface: pygame.Surface):
        # Define a font
        font = pygame.font.SysFont("arial", int(self.width * 0.3))

        # Define the button rectangle
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Draw the button
        pygame.draw.rect(surface, self.color, button_rect)

        # Draw the button text
        if self.button_text:
            button_text_surface = font.render(self.button_text, True, pygame.Color('black'))
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
    color: Tuple[int, int, int] | str = (255, 255, 255)
    flagged: bool = False

    def is_over(self, mouse_position: tuple[int, int]) -> bool:
        button_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return button_rect.collidepoint(mouse_position)

    def draw(self, screen, outline: bool = False):
        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.size, self.size))
        if outline:
            pygame.draw.rect(screen, color=(0, 0, 0), rect=(self.x, self.y, self.size, self.size), width=1)

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
            pygame.draw.rect(screen, color=(0, 0, 0), rect=(self.x, self.y, self.size, self.size), width=1)
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

    def draw(self, screen, outline: bool = False):

        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.size, self.size))
        if outline:
            pygame.draw.rect(screen, color=(0, 0, 0), rect=(self.x, self.y, self.size, self.size), width=1)
        if not self.hidden:
            font = pygame.font.SysFont("arial", 12)
            img = font.render(str(self.bomb_count), True, "black")
            screen.blit(img, (self.x + self.size / 2, self.y + self.size / 2))

    def reveal(self):
        self.hidden = False
        self.color = "green"
