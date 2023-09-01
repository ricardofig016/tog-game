import pygame


class Window(object):
    def __init__(self, BG_IMAGE_PATH, CAPTION) -> None:
        pygame.init()
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.BG_IMAGE = self.load_and_resize_image(BG_IMAGE_PATH)
        pygame.display.set_caption(CAPTION)

    def load_and_resize_image(self, image_path) -> pygame.Surface:
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

    def draw_screen_segments(self) -> None:
        pass

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.BG_IMAGE, (0, 0))

            self.draw_screen_segments()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        return
