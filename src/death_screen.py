import pygame
from pygame import Surface

from classes import TextButton
from constants import GameState, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, SHADOW, TITLE_FONT
from game import Game
from state_machine import state


class DeathScreen:
    window: Surface
    game: Game
    __restart_button: TextButton
    __main_menu: TextButton
    __quite_button: TextButton
    title: str = "GAME OVER"

    def __init__(self, window, game):
        self.window = window
        self.game = game
        self.create_buttons()

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.set_state(GameState.EXIT)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    mouse_position = pygame.mouse.get_pos()
                    if self.__restart_button.is_over(mouse_position):
                        self.game.reset_board()
                        state.set_state(GameState.GAME)
                    if self.__main_menu.is_over(mouse_position):
                        self.game.reset_board()
                        state.set_state(GameState.MENU)
                    if self.__quite_button.is_over(mouse_position):
                        state.set_state(GameState.EXIT)
        self.__restart_button.draw(self.window)
        self.__main_menu.draw(self.window)
        self.__quite_button.draw(self.window)
        self.render_title()

    def create_buttons(self):
        # Middle of screen
        button_x = (WINDOW_WIDTH // 2) - (TextButton.width // 2)
        button_y_top = WINDOW_HEIGHT * 0.3
        button_spacing = TextButton.height + 50

        self.__restart_button = (
            TextButton(x=button_x, y=button_y_top, button_text="Restart"))
        self.__main_menu = (
            TextButton(x=button_x, y=button_y_top + button_spacing, button_text="Menu"))
        self.__quite_button = (
            TextButton(x=button_x, y=button_y_top + (2 * button_spacing), button_text="Quit"))

    def render_title(self):
        # render the text using the custom font
        title_text = TITLE_FONT.render(self.title, True, BLACK)
        title_text_shadow = TITLE_FONT.render(self.title, True, SHADOW)
        self.window.blit(title_text_shadow,
                         (((WINDOW_WIDTH // 2) - title_text.get_width() // 2) + 3, (WINDOW_HEIGHT // 20) - 3))

        self.window.blit(title_text, ((WINDOW_WIDTH // 2) - title_text.get_width() // 2, WINDOW_HEIGHT // 20))
