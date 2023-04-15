from dataclasses import dataclass

from GameTimer import timer
from globals import GameState
from screen import Screen


@dataclass
class StateMachine:
    screen: Screen = None
    game_running: bool = True

    def exit_game(self):
        self.game_running = False

    def set_screen(self, screen: GameState):
        self.screen = screen

    def get_screen(self) -> GameState:
        return self.screen


# Global state class instance, can use dependency injection later on if it gets to complex
state = StateMachine()
