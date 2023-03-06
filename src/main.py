import pygame

from constants import GameState, SCREEN
from game import Game
from main_menu import MainMenu
from state_machine import state


def main():
    # Initialize classes
    main_menu = MainMenu()
    game = Game()
    while state.get_state() != GameState.EXIT:
        SCREEN.fill((255, 255, 255))
        match state.get_state():
            case GameState.MENU:
                main_menu.render()
            case GameState.GAME:
                game.run()
            case _:
                state.set_state(GameState.EXIT)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
