import pygame

from constants import GameState, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND
from death_screen import DeathScreen
from game import Game
from main_menu import MainMenu
from state_machine import state


def main():
    pygame.display.set_caption('PySweeper v0.1')
    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Initialize classes
    main_menu = MainMenu(main_window)
    game = Game(window=main_window)
    death_screen = DeathScreen(window=main_window, game=game)

    while state.get_state() != GameState.EXIT:
        # Blit the game window onto the screen
        main_window.fill(BACKGROUND)
        match state.get_state():
            case GameState.MENU:
                main_menu.render()
            case GameState.GAME:
                game.run()
            case GameState.GAME_OVER:
                death_screen.render()
            case _:
                state.set_state(GameState.EXIT)
        # Update the display
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
