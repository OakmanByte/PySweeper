from dataclasses import dataclass

import pygame
from pygame import Surface

from classes import MenuButton
from constants import GameState, WINDOW_WIDTH, WINDOW_HEIGHT
from state_machine import state


@dataclass
class MainMenu:
    window: Surface
    __start_button: MenuButton
    __quite_button: MenuButton
    title: str = "WELCOME"

    def __post_init__(self):
        self.create_elements()

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.set_state(GameState.EXIT)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    mouse_position = pygame.mouse.get_pos()
                    if self.__quite_button.is_over(mouse_position):
                        state.set_state(GameState.EXIT)
                    if self.__start_button.is_over(mouse_position):
                        state.set_state(GameState.GAME)
        self.__start_button.draw(self.window)
        self.__quite_button.draw(self.window)

    def create_elements(self):
        self.__start_button = (MenuButton(x=WINDOW_WIDTH / 2, y=WINDOW_HEIGHT / 4, color="gray", button_text="Start"))
        self.__quite_button = (MenuButton(x=WINDOW_WIDTH / 2, y=WINDOW_HEIGHT / 3, color="gray", button_text="Quit"))
