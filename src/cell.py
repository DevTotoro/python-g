from pygame import Surface, display
from pygame.math import Vector2


class Cell:
    def __init__(self, position: Vector2, size: int, surface: Surface = None) -> None:
        self.position = position
        self.surface = surface

        self.__size = size

    def draw(self, screen: display) -> None:
        screen.blit(self.surface, self.position * self.__size)
