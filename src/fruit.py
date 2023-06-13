from random import randint

from cell import Cell
from pygame.math import Vector2
from pygame import Surface, image, display
from typing import List


def generate_position(max_x: int, max_y: int, snake_body: List[Cell]) -> Vector2:
    while True:
        pos = Vector2(randint(0, max_x), randint(0, max_y))

        if pos not in [cell.position for cell in snake_body]:
            break

    return pos


class Fruit(Cell):
    def __init__(self, size: int, max_x: int, max_y: int, snake_body: List[Cell], asset_path: str):
        super().__init__(
            position=generate_position(max_x=max_x, max_y=max_y, snake_body=snake_body),
            size=size,
            surface=image.load(f'{asset_path}/sprites/apple.png').convert_alpha()
        )

    def __del__(self) -> None:
        print('Fruit eaten!')
