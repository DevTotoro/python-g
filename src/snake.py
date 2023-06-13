from cell import Cell
from pygame.math import Vector2
from pygame import Surface, image, display
from typing import Dict


ASSET_FILENAMES = {
    'head': {
        'up': 'head_up.png',
        'down': 'head_down.png',
        'left': 'head_left.png',
        'right': 'head_right.png'
    },
    'body': {
        'vertical': 'body_vertical.png',
        'horizontal': 'body_horizontal.png',
        'top_left': 'body_tl.png',
        'top_right': 'body_tr.png',
        'bottom_left': 'body_bl.png',
        'bottom_right': 'body_br.png'
    },
    'tail': {
        'up': 'tail_up.png',
        'down': 'tail_down.png',
        'left': 'tail_left.png',
        'right': 'tail_right.png'
    }
}


def load_assets(asset_path: str) -> Dict[str, Dict[str, Surface]]:
    assets = {}

    for asset_type in ASSET_FILENAMES:
        assets[asset_type] = {}

        for asset_direction in ASSET_FILENAMES[asset_type]:
            assets[asset_type][asset_direction] = image.load(
                f'{asset_path}/{asset_type}/{ASSET_FILENAMES[asset_type][asset_direction]}'
            ).convert_alpha()

    return assets


class Snake:
    def __init__(self, cell_size: int, asset_path: str) -> None:
        self.__cell_size = cell_size

        self.__assets = load_assets(asset_path=f'{asset_path}/sprites/snake')

        self.__body = []
        self.__direction = Vector2(0, 0)
        self.reset()

    def draw(self, screen: display) -> None:
        self.__update_head_asset()
        self.__update_tail_asset()

        for i in range(1, len(self.__body) - 1):
            self.__update_body_asset(index=i, cell=self.__body[i])

        for cell in self.__body:
            cell.draw(screen=screen)

    def move(self) -> None:
        for i in range(len(self.__body) - 1, 0, -1):
            self.__body[i].position = Vector2(self.__body[i - 1].position)

        self.__body[0].position += self.__direction

    def set_direction(self, direction: Vector2) -> None:
        if self.__direction + direction != Vector2(0, 0):
            self.__direction = direction

    def grow(self) -> None:
        tail = self.__body[-1]
        new_tail = Cell(position=Vector2(tail.position), size=self.__cell_size, surface=tail.surface)

        if tail.position.x < self.__body[-2].position.x:
            new_tail.position.x -= 1
        elif tail.position.x > self.__body[-2].position.x:
            new_tail.position.x += 1
        elif tail.position.y < self.__body[-2].position.y:
            new_tail.position.y -= 1
        elif tail.position.y > self.__body[-2].position.y:
            new_tail.position.y += 1

        self.__body.append(new_tail)

    def get_body(self) -> list[Cell]:
        return self.__body

    def reset(self) -> None:
        self.__direction = Vector2(1, 0)

        self.__body = [
            Cell(position=Vector2(5, 10), size=self.__cell_size, surface=self.__assets['head']['right']),
            Cell(position=Vector2(4, 10), size=self.__cell_size, surface=self.__assets['body']['horizontal']),
            Cell(position=Vector2(3, 10), size=self.__cell_size, surface=self.__assets['tail']['left'])
        ]

    def __update_head_asset(self) -> None:
        if self.__direction == Vector2(1, 0):
            self.__body[0].surface = self.__assets['head']['right']
        elif self.__direction == Vector2(-1, 0):
            self.__body[0].surface = self.__assets['head']['left']
        elif self.__direction == Vector2(0, 1):
            self.__body[0].surface = self.__assets['head']['down']
        elif self.__direction == Vector2(0, -1):
            self.__body[0].surface = self.__assets['head']['up']

    def __update_tail_asset(self) -> None:
        if self.__body[-2].position.x < self.__body[-1].position.x:
            self.__body[-1].surface = self.__assets['tail']['right']
        elif self.__body[-2].position.x > self.__body[-1].position.x:
            self.__body[-1].surface = self.__assets['tail']['left']
        elif self.__body[-2].position.y < self.__body[-1].position.y:
            self.__body[-1].surface = self.__assets['tail']['down']
        elif self.__body[-2].position.y > self.__body[-1].position.y:
            self.__body[-1].surface = self.__assets['tail']['up']

    def __update_body_asset(self, index: int, cell: Cell) -> None:
        previous_cell_rel_pos = self.__body[index - 1].position - cell.position
        next_cell_rel_pos = self.__body[index + 1].position - cell.position

        if previous_cell_rel_pos.x == next_cell_rel_pos.x:
            self.__body[index].surface = self.__assets['body']['vertical']
        elif previous_cell_rel_pos.y == next_cell_rel_pos.y:
            self.__body[index].surface = self.__assets['body']['horizontal']
        else:
            if previous_cell_rel_pos.x == -1 and next_cell_rel_pos.y == -1 or \
                    previous_cell_rel_pos.y == -1 and next_cell_rel_pos.x == -1:
                self.__body[index].surface = self.__assets['body']['top_left']
            elif previous_cell_rel_pos.x == 1 and next_cell_rel_pos.y == -1 or \
                    previous_cell_rel_pos.y == -1 and next_cell_rel_pos.x == 1:
                self.__body[index].surface = self.__assets['body']['top_right']
            elif previous_cell_rel_pos.x == -1 and next_cell_rel_pos.y == 1 or \
                    previous_cell_rel_pos.y == 1 and next_cell_rel_pos.x == -1:
                self.__body[index].surface = self.__assets['body']['bottom_left']
            elif previous_cell_rel_pos.x == 1 and next_cell_rel_pos.y == 1 or \
                    previous_cell_rel_pos.y == 1 and next_cell_rel_pos.x == 1:
                self.__body[index].surface = self.__assets['body']['bottom_right']
