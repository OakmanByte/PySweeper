import itertools
from dataclasses import dataclass

import pygame

from classes import MenuButton
from constants import GameState, WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN
from state_machine import state


@dataclass
class MainMenu:
    start_button: MenuButton
    quite_button: MenuButton
    title: str = "WELCOME"

    def __init__(self):
        self.create_elements()

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.set_state(GameState.EXIT)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    mouse_position = pygame.mouse.get_pos()
                    if self.quite_button.is_over(mouse_position):
                        state.set_state(GameState.EXIT)
                    if self.start_button.is_over(mouse_position):
                        state.set_state(GameState.GAME)
        self.start_button.draw(SCREEN)
        self.quite_button.draw(SCREEN)

    def create_elements(self):
        self.start_button = (MenuButton(x=WINDOW_WIDTH / 2, y=WINDOW_HEIGHT / 4, color="gray", button_text="Start"))
        self.quite_button = (MenuButton(x=WINDOW_WIDTH / 2, y=WINDOW_HEIGHT / 3, color="gray", button_text="Quit"))
