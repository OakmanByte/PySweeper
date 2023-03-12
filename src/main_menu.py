import pygame
from pygame import Surface
from pygame.event import Event

from classes import TextButton
from constants import GameState, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, SHADOW, TITLE_FONT
from state_machine import state


class MainMenu:
    __buttons: [TextButton] = []

    def __init__(self, window: Surface, title: str):
        self.window = window
        self.title = title
        self.create_buttons()
        self.title_text = TITLE_FONT.render(self.title, True, BLACK)
        self.title_text_shadow = TITLE_FONT.render(self.title, True, SHADOW)

    def render(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                mouse_position = pygame.mouse.get_pos()
                for button in self.__buttons:
                    button.is_over(mouse_position)

        self.render_title()
        self.render_buttons()

    def create_buttons(self):
        # Middle of screen
        button_x = (WINDOW_WIDTH // 2) - (TextButton.width // 2)
        button_y_top = WINDOW_HEIGHT * 0.3
        button_spacing = TextButton.height + 50

        self.__buttons.append(
            TextButton(x=button_x, y=button_y_top, button_text="Start",
                       on_click_func=(lambda: state.set_state(GameState.GAME))))
        self.__buttons.append(
            TextButton(x=button_x, y=button_y_top + button_spacing, button_text="Options",
                       on_click_func=(lambda: state.set_state(GameState.GAME))))
        self.__buttons.append(
            TextButton(x=button_x, y=button_y_top + (2 * button_spacing), button_text="Quit",
                       on_click_func=(lambda: state.set_state(GameState.EXIT))))

    def render_buttons(self):
        for button in self.__buttons:
            button.draw(self.window)

    def render_title(self):
        self.window.blit(self.title_text_shadow,
                         (((WINDOW_WIDTH // 2) - self.title_text.get_width() // 2) + 3, (WINDOW_HEIGHT // 20) - 3))

        self.window.blit(self.title_text, ((WINDOW_WIDTH // 2) - self.title_text.get_width() // 2, WINDOW_HEIGHT // 20))
