import pygame
from pygame import Surface

from classes import TextButton, RadioButtonGroup, RadioButton
from constants import GameState, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, SHADOW, TITLE_FONT
from state_machine import state
import pygame_menu


class MainMenu:
    window: Surface
    __start_button: TextButton
    __options_button: TextButton
    __quit_button: TextButton
    __radio_button_group: RadioButtonGroup
    title: str = "Welcome to PySweeper!"

    def __init__(self, window):
        self.window = window
        self.create_buttons()
        self.create_radio_button_group()
        self.title_text = TITLE_FONT.render(self.title, True, BLACK)
        self.title_text_shadow = TITLE_FONT.render(self.title, True, SHADOW)

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.set_state(GameState.EXIT)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    mouse_position = pygame.mouse.get_pos()
                    if self.__quit_button.is_over(mouse_position):
                        state.set_state(GameState.EXIT)
                    if self.__start_button.is_over(mouse_position):
                        state.set_state(GameState.GAME)
        self.__start_button.draw(self.window)
        self.__options_button.draw(self.window)
        self.__quit_button.draw(self.window)
        self.render_title()
        self.__radio_button_group.draw(self.window)

    def create_buttons(self):
        # Middle of screen
        button_x = (WINDOW_WIDTH // 2) - (TextButton.width // 2)
        button_y_top = WINDOW_HEIGHT * 0.3
        button_spacing = TextButton.height + 50

        self.__start_button = (
            TextButton(x=button_x, y=button_y_top, button_text="Start"))
        self.__options_button = (
            TextButton(x=button_x, y=button_y_top + button_spacing, button_text="Options"))
        self.__quit_button = (
            TextButton(x=button_x, y=button_y_top + (2 * button_spacing), button_text="Quit"))

    def render_title(self):
        self.window.blit(self.title_text_shadow,
                         (((WINDOW_WIDTH // 2) - self.title_text.get_width() // 2) + 3, (WINDOW_HEIGHT // 20) - 3))

        self.window.blit(self.title_text, ((WINDOW_WIDTH // 2) - self.title_text.get_width() // 2, WINDOW_HEIGHT // 20))

    def create_radio_button_group(self):
        dimension_options = ["6X6", "8X8", "12X12", "16X16"]
        button_spacing = TextButton.width // 2

        # Middle of screen
        button_x = (WINDOW_WIDTH // 2) - ((RadioButton.width // 2) * len(dimension_options)) + button_spacing
        button_y_top = WINDOW_HEIGHT * 0.2

        radio_buttons: [RadioButton] = []
        for i, option in enumerate(dimension_options):
            radio_buttons.append(RadioButton(x=button_x + (button_spacing * i), y=button_y_top, button_text=option))

        self.__radio_button_group: RadioButtonGroup = RadioButtonGroup(buttons=radio_buttons)
        print(radio_buttons)

    @staticmethod
    def set_board_dimension(dimension, difficulty):
        print("Selected difficulty: %s", dimension)
