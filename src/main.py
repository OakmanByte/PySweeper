import pygame

from constants import GameState, WINDOW_WIDTH, WINDOW_HEIGHT, GAME_WIDTH, GAME_HEIGHT, BACKGROUND
from game import Game
from main_menu import MainMenu
from state_machine import state


def main():
    pygame.display.set_caption('PySweeper v0.1')
    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Initialize classes
    main_menu = MainMenu(main_window)
    game = Game(window=main_window)

    while state.get_state() != GameState.EXIT:
        # Blit the game window onto the screen
        main_window.fill(BACKGROUND)
        match state.get_state():
            case GameState.MENU:
                main_menu.render()
            case GameState.GAME:
                game.run()
            case _:
                state.set_state(GameState.EXIT)
        # Update the display
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
