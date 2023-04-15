from abc import ABC, abstractmethod
from pygame.event import Event


class Screen(ABC):
    @abstractmethod
    def render(event: Event):
        pass
    