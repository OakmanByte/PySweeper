from dataclasses import dataclass
import pygame


@dataclass
class Button:
    x: int = 0
    y: int = 0
    width: int = 64
    height: int = 64
    color: tuple[int, int, int] = (0, 0, 0)

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
