import pygame


class Game:
    def __init__(self, title: str = "Game", cells_x: int = 10, cells_y: int = 10, cell_size: int = 50):
        pygame.init()

        self.__screen = pygame.display.set_mode((cells_x * cell_size, cells_y * cell_size))
        pygame.display.set_caption(title)
        print('=====================')
        print(f'Initialized game with title "{title}" and size {cells_x * cell_size}x{cells_y * cell_size}.')

        self.__clock = pygame.time.Clock()
        self.__dt = 0

        self.__is_running = True

    def __del__(self):
        pygame.quit()

    def run(self):
        while self.__is_running:
            # Exit conditions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_running = False
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.__is_running = False
                    return

            self.__update()
            self.__draw()

            self.__dt = self.__clock.tick(60) / 1000

    def __update(self):
        # Get pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print("w")
        if keys[pygame.K_s]:
            print("s")
        if keys[pygame.K_a]:
            print("a")
        if keys[pygame.K_d]:
            print("d")

    def __draw(self):
        self.__screen.fill("black")

        pygame.display.flip()
