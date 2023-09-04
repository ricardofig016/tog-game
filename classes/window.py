import pygame


class Window(object):
    YELLOW = (255, 255, 0)
    BLUE = (76, 255, 209)
    DARK_GRAY = (50, 50, 50)
    LIGHT_GRAY = (220, 220, 220)

    def __init__(self, bg_image_path, caption) -> None:
        pygame.init()
        self.WIDTH = 1500
        self.HEIGHT = 1000
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.TEXT_COLOR = self.LIGHT_GRAY
        self.clock = pygame.time.Clock()
        self.bg_image = self.load_and_resize_image(
            bg_image_path, self.WIDTH, self.HEIGHT
        )
        pygame.display.set_caption(caption)

    def load_and_resize_image(
        self, image_path: str, width: int, height: int
    ) -> pygame.Surface:
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (width, height))

    def render_text(
        self,
        text: str,
        font_size: int,
        color: (int, int, int) = (255, 255, 255),
        font_fam: str = None,
        bg_color: (int, int, int) = None,
    ) -> pygame.Surface:
        font = pygame.font.Font(font_fam, font_size)
        return font.render(text, True, color, bg_color)

    def blit_text(
        self, text_surface: pygame.Surface, x: int, y: int, align: str = None
    ) -> None:
        if align == "left":
            align_mult = (0, -0.5)
        elif align == "right":
            align_mult = (-1, -0.5)
        elif align == "top":
            align_mult = (-0.5, 0)
        elif align == "bottom":
            align_mult = (-0.5, -1)
        elif align == "center":
            align_mult = (-0.5, -0.5)
        else:
            align_mult = (0, 0)

        self.screen.blit(
            text_surface,
            (
                int(x + text_surface.get_width() * align_mult[0]),
                int(y + text_surface.get_height() * align_mult[1]),
            ),
        )
        return

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
