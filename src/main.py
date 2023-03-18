import pygame

from death_screen import DeathScreen
from game import Game
from globals import GameState, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND
from main_menu import MainMenu
from state_machine import state
from win_screen import WinScreen


def main():
    pygame.display.set_caption('PySweeper v0.1')
    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # Initialize classes
    main_menu = MainMenu(main_window, "Welcome to PySweeper!")
    game = Game(main_window)
    death_screen = DeathScreen(window=main_window, game=game)
    win_screen = WinScreen(window=main_window, game=game)

    while state.get_state() != GameState.EXIT:

        # Process events if there are any, otherwise add a fallback event
        # This way we can still render the different screen even if there is no events, necessary for example the timer
        events = pygame.event.get()
        if not events:
            events.append(pygame.event.Event(pygame.USEREVENT))

        for event in events:
            if event.type == pygame.QUIT:
                state.set_state(GameState.EXIT)
            main_window.fill(BACKGROUND)
            match state.get_state():
                case GameState.MENU:
                    main_menu.render(event)
                case GameState.GAME:
                    game.run(event)
                case GameState.GAME_OVER:
                    death_screen.render(event)
                case GameState.WIN:
                    win_screen.render(event)
                case _:
                    state.set_state(GameState.EXIT)
            pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
