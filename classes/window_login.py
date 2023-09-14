import pygame
from classes.window import Window
from classes.player import Player


class Login(Window):
    def __init__(self) -> None:
        bg_image_path = "assets/login_window/bg.png"
        caption = "Welcome"
        super().__init__(bg_image_path, caption)

    def blit_start_text(self) -> None:
        text = "[click anywhere to continue]"
        text_surface = self.render_text(text, int(self.WIDTH * 0.05), self.DARK_GRAY)
        self.blit_text(text_surface, 0.5 * self.WIDTH, 0.05 * self.HEIGHT, "center")
        return

    def blit_center_rect(self) -> None:
        x = 1 / 4 * self.WIDTH
        y = 1 / 4 * self.HEIGHT
        width = 1 / 2 * self.WIDTH
        height = 1 / 2 * self.HEIGHT
        pygame.draw.rect(self.screen, self.DARK_GRAY, (x, y, width, height))
        return

    def blit_login(self, username):
        self.blit_center_rect()

        text = self.render_text("Log In", int(self.WIDTH * 0.06), self.TEXT_COLOR)
        self.blit_text(text, 0.5 * self.WIDTH, 0.4 * self.HEIGHT, "center")

        x = 1 / 3 * self.WIDTH
        y = 11 / 20 * self.HEIGHT
        width = 1 / 3 * self.WIDTH
        height = 1 / 20 * self.HEIGHT
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, (x, y, width, height))

        text = self.render_text(username, int(self.WIDTH * 0.03), self.DARK_GRAY)
        self.blit_text(text, 0.5 * self.WIDTH, 23 / 40 * self.HEIGHT, "center")

        return

    def start_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
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

    def login_loop(self) -> str:
        running = True
        username = ""
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalnum():
                        if len(username) <= 20:
                            username += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    if event.key == pygame.K_RETURN and len(username) > 0:
                        running = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return ""
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return ""

            self.screen.blit(self.bg_image, (0, 0))
            self.blit_login(username)

            pygame.display.update()
            self.clock.tick(60)
        return username

    def run(self) -> Player:
        self.start_loop()
        username = self.login_loop()
        if not username:
            return
        player = Player(username)

        pygame.quit()
        return player
