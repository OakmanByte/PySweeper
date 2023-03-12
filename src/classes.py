from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Optional, Callable
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from constants import item_size, GameState, BLACK, WHITE, BUTTON_FONT, NUMBER_BOARD_ITEM_FONT
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
    border_radius: int = 20
    color: Tuple[int, int, int] | str = WHITE
    on_click_func: Optional[Callable[[], None]] = None

    def draw(self, surface: pygame.Surface):
        # Define the button rectangle
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Draw the button
        pygame.draw.rect(surface, self.color, button_rect, border_radius=self.border_radius)

        # Draw the button text
        if self.button_text:
            button_text_surface = self.font.render(self.button_text, True, pygame.Color('black'))
            text_x = button_rect.x + (button_rect.width - button_text_surface.get_width()) // 2
            text_y = button_rect.y + (button_rect.height - button_text_surface.get_height()) // 2
            surface.blit(button_text_surface, (text_x, text_y))

    def is_over(self, mouse_position: Tuple[int, int]):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if button_rect.collidepoint(mouse_position):
            self.on_click()

    def on_click(self):
        if self.on_click_func:
            self.on_click_func()

    def set_on_click(self, func: Optional[Callable[[], None]]):
        self.on_click_func = func


@dataclass
class BoardItem:
    type: BoardItemTypes
    hidden: bool = True
    x: int = 0
    y: int = 0
    size: int = item_size
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
        if self.hidden:
            self.flagged = not self.flagged

    def get_flag_image_and_location(self) -> Tuple[Surface, Rect]:
        # Load the image
        flag_image = pygame.image.load('flag.svg')
        img_rect = flag_image.get_rect(center=(self.x + self.size / 2, self.y + self.size / 2))
        # Draw the image onto the screen
        return flag_image, img_rect


@dataclass
class Bomb(BoardItem):
    type: BoardItemTypes = BoardItemTypes.BOMB

    def draw(self, screen, outline: bool = False):
        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.size, self.size))
        if outline:
            pygame.draw.rect(screen, color=BLACK, rect=(self.x, self.y, self.size, self.size), width=1)
        if self.flagged:
            screen.blit(*self.get_flag_image_and_location())

    def reveal(self):
        if not self.flagged:
            self.hidden = False
            self.color = "red"
            state.set_state(GameState.GAME_OVER)


@dataclass
class Number(BoardItem):
    type: BoardItemTypes = BoardItemTypes.NUMBER
    bomb_count: int = 0
    font: Font = NUMBER_BOARD_ITEM_FONT

    def draw(self, screen, outline: bool = False):
        pygame.draw.rect(screen, color=self.color, rect=(self.x, self.y, self.size, self.size))
        if outline:
            pygame.draw.rect(screen, color=BLACK, rect=(self.x, self.y, self.size, self.size), width=1)
        if not self.hidden:
            bombs_count_img = self.font.render(str(self.bomb_count), True, BLACK)
            img_rect = bombs_count_img.get_rect(center=(self.x + self.size / 2, self.y + self.size / 2))
            screen.blit(bombs_count_img, img_rect)
        if self.flagged:
            screen.blit(*self.get_flag_image_and_location())

    def reveal(self):
        if not self.flagged:
            self.hidden = False
            self.color = "green"
