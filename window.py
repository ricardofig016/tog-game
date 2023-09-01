import pygame


class Window(object):
    def __init__(self, bg_image_path, caption) -> None:
        pygame.init()
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.GRID_CELL_SIZE = 60
        self.WHITE = (255, 255, 255)
        self.GRID_COLOR = (100, 100, 100)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load(bg_image_path)
        pygame.display.set_caption(caption)

    def draw_screen_segments(self) -> None:
        pass

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background_image, (0, 0))

            self.draw_screen_segments()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        return
