from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import pygame


class BoardItemTypes(Enum):
    BOMB = "Bomb"
    NUMBER = "Number"


@dataclass
class BoardItem:
    type: BoardItemTypes
    hidden: bool = True
    x: int = 0
    y: int = 0
    width: int = 64
    height: int = 64
    color: Tuple[int, int, int] | str = (255, 255, 255)

    def is_over(self, mouse_position: tuple[int, int]):
        return self.x <= mouse_position[0] <= (self.x + self.width) \
               and self.y <= mouse_position[1] <= (self.y + self.height)

    def draw(self, screen, outline: bool = False):
        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.width, self.height))
        if outline:
            pygame.draw.rect(screen, color=(0, 0, 0), rect=(self.x, self.y, self.width, self.height), width=1)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def reveal(self):
        self.hidden = False


@dataclass
class Bomb(BoardItem):
    type: BoardItemTypes = BoardItemTypes.BOMB

    def draw(self, screen, outline: bool = False):
        color = "white" if self.hidden else "red"
        pygame.draw.rect(screen, color=color, rect=(self.x, self.y, self.width, self.height))
        if outline:
            pygame.draw.rect(screen, color=(0, 0, 0), rect=(self.x, self.y, self.width, self.height), width=1)

    def reveal(self):
        self.hidden = False
        self.color = "red"


@dataclass
class Number(BoardItem):
    type: BoardItemTypes = BoardItemTypes.NUMBER
    bomb_count: int = 5

    def draw(self, screen, outline: bool = False):
        color = "white" if self.hidden else "green"
        pygame.draw.rect(screen, color=color, rect=(self.x, self.y, self.width, self.height))
        if outline:
            pygame.draw.rect(screen, color=(0, 0, 0), rect=(self.x, self.y, self.width, self.height), width=1)

        font = pygame.font.SysFont("arial", 24)
        img = font.render(str(self.bomb_count), True, "black")
        screen.blit(img, (self.x + self.width / 2, self.y + self.height / 2))


def reveal(self):
    self.hidden = False
    self.color = "green"
