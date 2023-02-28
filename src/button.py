from dataclasses import dataclass
import pygame
from pygame import Surface, SurfaceType


@dataclass
class Button:
    x: int
    y: int
    width: int
    height: int
    color: tuple[int, int, int] = (0, 0, 0)
    icon_path: str = None
    icon: Surface | SurfaceType = None

    def __post_init__(self):
        if self.icon_path:
            self.icon = pygame.image.load(self.icon_path)

    def is_over(self, mouse_position: tuple[int, int]):
        return self.x <= mouse_position[0] <= (self.x + self.width) \
               and self.y <= mouse_position[1] <= (self.y + self.height)

    def draw(self, screen):
        if self.icon:
            screen.blit(self.icon, (self.x, self.y))
        else:
            pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.width, self.height))


@dataclass
class Bomb(Button):

    def __post_init__(self):
        self.icon = pygame.image.load("gift.svg")

    def on_click(self):
        print("boom!")
