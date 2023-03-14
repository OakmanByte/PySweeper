from dataclasses import dataclass

import pygame


@dataclass
class GameTimer:
    time: int = pygame.time.get_ticks()

    def start_timer(self):
        self.time = pygame.time.get_ticks()

    def get_start_time(self):
        return self.time

    def get_elapsed_time_str_formatted(self):
        return f"Time: {(pygame.time.get_ticks() - self.time) // 1000}s"


# Global timer  class instance, can use dependency injection later on if it gets to complex
timer = GameTimer()
