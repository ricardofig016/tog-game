import pygame
from classes.window import Window


class Login(Window):
    def __init__(self) -> None:
        bg_image_path = "assets/login_window/bg.png"
        caption = "Welcome"
        super().__init__(bg_image_path, caption)

    def blit_start_text(self) -> None:
        text = "[click anywhere to continue]"
        text_surface = self.render_text(text, int(self.WIDTH * 0.032), self.DARK_GRAY)
        self.blit_text(text_surface, 0.5 * self.WIDTH, 0.05 * self.HEIGHT, "center")
        return

    def blit_center_rect(self) -> None:
        x = 1 / 4 * self.WIDTH
        y = 1 / 4 * self.HEIGHT
        width = 1 / 2 * self.WIDTH
        height = 1 / 2 * self.HEIGHT
        pygame.draw.rect(self.screen, self.DARK_GRAY, (x, y, width, height))
        return

    def blit_login_options(self):
        self.blit_center_rect()

    def start_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.blit(self.bg_image, (0, 0))
            self.blit_start_text()

            pygame.display.update()
            self.clock.tick(60)
        return

    def login_option_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.bg_image, (0, 0))
            self.blit_login_options()

            pygame.display.update()
            self.clock.tick(60)
        return

    def run(self) -> None:
        self.start_loop()
        opt = self.login_option_loop()
        if opt == 3:
            pass

        pygame.quit()
        return
