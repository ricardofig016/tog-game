import pygame
from classes.window import Window


class Tutorial(Window):
    def __init__(self, bg_image_path, caption, text) -> None:
        self.text = text
        super().__init__(bg_image_path, caption=caption)

    def blit_rect(self) -> None:
        x = 1 / 8 * self.WIDTH
        y = 1 / 8 * self.HEIGHT
        width = 3 / 4 * self.WIDTH
        height = 3 / 4 * self.HEIGHT
        pygame.draw.rect(self.screen, self.DARK_GRAY, (x, y, width, height))

        pygame.draw.line(self.screen, self.LIGHT_GRAY, (x, y), (x + width, y), 4)
        pygame.draw.line(
            self.screen, self.LIGHT_GRAY, (x, y + height), (x + width, y + height), 4
        )
        pygame.draw.line(self.screen, self.LIGHT_GRAY, (x, y), (x, y + height), 4)
        pygame.draw.line(
            self.screen, self.LIGHT_GRAY, (x + width, y), (x + width, y + height), 4
        )

        text = "[click anywhere to continue]"
        text_surface = self.render_text(text, int(self.WIDTH * 0.03), self.TEXT_COLOR)
        self.blit_text(text_surface, 0.5 * self.WIDTH, 0.83 * self.HEIGHT, "center")
        return

    def blit_lines(self, lines: [str]) -> None:
        for line in lines:
            pass
        return

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.blit(self.bg_image, (0, 0))
            self.blit_rect()
            lines = self.divide_text_in_lines(self.text, 15)
            self.blit_lines(lines)

            pygame.display.update()
            self.clock.tick(60)
        return
