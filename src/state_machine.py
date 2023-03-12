from dataclasses import dataclass

from GameTimer import timer
from constants import GameState
from main import game

initial_state = GameState.MENU


@dataclass
class StateMachine:
    state: GameState = GameState.MENU

    def set_state(self, _state: GameState):
        # Reset game timer, TODO: better place to do this?
        if _state == GameState.GAME:
            timer.start_timer()
            game.reset_board()
        self.state = _state

    def get_state(self) -> GameState:
        return self.state


# Global state class instance, can use dependency injection later on if it gets to complex
state = StateMachine()
