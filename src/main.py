import pygame

from constants import GameState
from game import Game
from state_machine import state


def main():
    # Initialize game class and board
    game = Game()
    while state.get_state() != GameState.EXIT:
        match state.get_state():
            case GameState.MENU:
                game.run_game()
            case GameState.GAME:
                game.run_game()
            case _:
                state.set_state(GameState.EXIT)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
