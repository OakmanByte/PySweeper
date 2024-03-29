import pygame
from pygame import Surface
from pygame.event import Event

from classes import TextButton
import game
from globals import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, SHADOW, TITLE_FONT
import main_menu
from state_machine import state
from screen import Screen


class DeathScreen(Screen):
    window: Surface
    __buttons: [TextButton] = []
    title: str = "GAME OVER"

    def __init__(self, window):
        self.window = window
        self.create_buttons()

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
            TextButton(x=button_x, y=button_y_top, button_text="Restart",
                       on_click_func=(lambda: state.set_screen(game.Game(self.window)))))
        self.__buttons.append(
            TextButton(x=button_x, y=button_y_top + button_spacing, button_text="Menu",
                       on_click_func=(lambda: state.set_screen(main_menu.MainMenu(self.window)))))
        self.__buttons.append(
            TextButton(x=button_x, y=button_y_top + (2 * button_spacing), button_text="Quit",
                       on_click_func=(lambda: state.exit_game())))

    def render_buttons(self):
        for button in self.__buttons:
            button.draw(self.window)

    def render_title(self):
        # render the text using the custom font
        title_text = TITLE_FONT.render(self.title, True, BLACK)
        title_text_shadow = TITLE_FONT.render(self.title, True, SHADOW)
        self.window.blit(title_text_shadow,
                         (((WINDOW_WIDTH // 2) - title_text.get_width() // 2) + 3, (WINDOW_HEIGHT // 20) - 3))

        self.window.blit(title_text, ((WINDOW_WIDTH // 2) - title_text.get_width() // 2, WINDOW_HEIGHT // 20))
