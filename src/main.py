import pygame

from globals import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND
from main_menu import MainMenu
from state_machine import state


def main():
    pygame.display.set_caption('PySweeper v0.1')
    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # Initialize classes
    main_menu = MainMenu(main_window)
    state.set_screen(main_menu)


    while state.game_running:

        # Process events if there are any, otherwise add a fallback event
        # This way we can still render the different screen even if there is no events, necessary for example the timer
        events = pygame.event.get()
        if not events:
            events.append(pygame.event.Event(pygame.USEREVENT))

        main_window.fill(BACKGROUND)
        for event in events:
            if event.type == pygame.QUIT:
                state.game_running = False
            else:
                state.get_screen().render(event)

        
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
