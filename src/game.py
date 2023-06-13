from os import path
import pygame
from pygame.math import Vector2

from snake import Snake
from fruit import Fruit


ASSET_PATH = path.join(path.dirname(__file__), '..', 'assets')


class Game:
    def __init__(self, title: str = "Game", cells_x: int = 10, cells_y: int = 10, cell_size: int = 40) -> None:
        self.__cells_x = cells_x
        self.__cells_y = cells_y
        self.__cell_size = cell_size

        pygame.init()

        self.__screen = pygame.display.set_mode((self.__cells_x * self.__cell_size, self.__cells_y * self.__cell_size))
        pygame.display.set_caption(title)
        print('=====================')
        print(f'Initialized game with title "{title}" and size {self.__cells_x * self.__cell_size}x{self.__cells_y * self.__cell_size}.')

        self.__clock = pygame.time.Clock()

        self.__is_running = True
        self.__game_over = False

        self.__snake = Snake(cell_size=self.__cell_size, asset_path=ASSET_PATH)
        self.__fruit = self.__spawn_fruit()

    def __del__(self) -> None:
        pygame.quit()

    def run(self, fps: int = 10) -> None:
        while self.__is_running:
            self.__process_events()

            if not self.__game_over:
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
                    case pygame.K_SPACE:
                        if self.__game_over:
                            self.__reset()
                    case pygame.K_w:
                        self.__snake.set_direction(direction=Vector2(0, -1))
                    case pygame.K_s:
                        self.__snake.set_direction(direction=Vector2(0, 1))
                    case pygame.K_a:
                        self.__snake.set_direction(direction=Vector2(-1, 0))
                    case pygame.K_d:
                        self.__snake.set_direction(direction=Vector2(1, 0))
                    case _:
                        pass

    def __update(self) -> None:
        self.__snake.move()

        self.__check_collisions()

    def __draw(self) -> None:
        self.__screen.fill((170, 215, 81))

        self.__snake.draw(screen=self.__screen)
        self.__fruit.draw(screen=self.__screen)

        pygame.display.flip()

    def __spawn_fruit(self) -> Fruit:
        return Fruit(
            size=self.__cell_size,
            max_x=self.__cells_x - 1,
            max_y=self.__cells_y - 1,
            snake_body=self.__snake.get_body(),
            asset_path=ASSET_PATH
        )

    def __check_collisions(self) -> None:
        # Check food collision
        if self.__snake.get_body()[0].position == self.__fruit.position:
            self.__snake.grow()
            self.__fruit = self.__spawn_fruit()

        # Check body collision
        for cell in self.__snake.get_body()[1:]:
            if self.__snake.get_body()[0].position == cell.position:
                self.__game_over = True

        # Check wall collision
        if self.__snake.get_body()[0].position.x < 0 or self.__snake.get_body()[0].position.x > self.__cells_x - 1:
            self.__game_over = True
        if self.__snake.get_body()[0].position.y < 0 or self.__snake.get_body()[0].position.y > self.__cells_y - 1:
            self.__game_over = True

    def __reset(self) -> None:
        self.__snake.reset()
        self.__fruit = self.__spawn_fruit()
        self.__game_over = False
