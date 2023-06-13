from os import path
import pygame
from pygame.math import Vector2

from cell import Cell


ASSETS_PATH = path.join(path.dirname(__file__), '..', 'assets')


class Game:
    def __init__(self, title: str = "Game", cells_x: int = 10, cells_y: int = 10, cell_size: int = 40) -> None:
        pygame.init()

        self.__screen = pygame.display.set_mode((cells_x * cell_size, cells_y * cell_size))
        pygame.display.set_caption(title)
        print('=====================')
        print(f'Initialized game with title "{title}" and size {cells_x * cell_size}x{cells_y * cell_size}.')

        self.__clock = pygame.time.Clock()

        self.__is_running = True

        self.cell = Cell(position=Vector2(19, 19), size=cell_size, surface=pygame.image.load(f'{ASSETS_PATH}/sprites/apple.png').convert_alpha())

    def __del__(self) -> None:
        pygame.quit()

    def run(self, fps: int = 10) -> None:
        while self.__is_running:
            self.__process_events()
            self.__update()
            self.__draw()

            self.__clock.tick(fps)

    def __process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False
                return
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        self.__is_running = False
                        return
                    case pygame.K_w:
                        print("w")
                    case pygame.K_s:
                        print("s")
                    case pygame.K_a:
                        print("a")
                    case pygame.K_d:
                        print("d")
                    case _:
                        pass

    def __update(self) -> None:
        pass

    def __draw(self) -> None:
        self.__screen.fill("white")

        self.cell.draw(screen=self.__screen)

        pygame.display.flip()
