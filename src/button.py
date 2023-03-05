from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import pygame

from constants import ITEM_SIZE


class BoardItemTypes(Enum):
    BOMB = "Bomb"
    NUMBER = "Number"


@dataclass
class BoardItem:
    type: BoardItemTypes
    hidden: bool = True
    x: int = 0
    y: int = 0
    size: int = ITEM_SIZE
    color: Tuple[int, int, int] | str = (255, 255, 255)
    flagged: bool = False

    def is_over(self, mouse_position: tuple[int, int]):
        return self.x <= mouse_position[0] <= (self.x + self.size) \
               and self.y <= mouse_position[1] <= (self.y + self.size)

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
    # TODO: Not working currently
    self.color = "green"
