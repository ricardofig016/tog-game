import pygame


class Window(object):
    def __init__(self, bg_image_path, caption) -> None:
        pygame.init()
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.bg_image = self.load_and_resize_image(
            bg_image_path, self.WIDTH, self.HEIGHT
        )
        pygame.display.set_caption(caption)

    def load_and_resize_image(self, image_path, width, height) -> pygame.Surface:
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (width, height))

    def draw_screen_segments(self) -> None:
        pass

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.bg_image, (0, 0))

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        return
