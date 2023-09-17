import pygame


class Window(object):
    RED = (230, 30, 30)
    GREEN = (50, 230, 50)
    YELLOW = (255, 255, 0)
    BLUE = (76, 255, 209)
    DARK_GRAY = (50, 50, 50)
    LIGHT_GRAY = (220, 220, 220)
    HEIGHT = 500  # default 900
    WIDTH = int(HEIGHT * 1.5)
    SLEEP_TIME = 0.3  # default 0.3

    def __init__(self, bg_image_path, caption) -> None:
        pygame.init()
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

    def divide_text_in_lines(self, text: str, line_size: int) -> [str]:
        lines = []
        words = text.split(" ")
        curr_line = ""
        for word in words:
            if len(curr_line) + len(word) + 1 <= line_size:
                curr_line += word + " "
            else:
                lines.append(curr_line)
                curr_line = word + " "
        lines.append(curr_line)
        print(lines)
        return lines

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
        """
        Args:
            align (str, optional): Can be "left", "right", "top", "bottom", "center". Defaults to None.
        """
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

    def blit_popup(self):
        x = 0
        y = 1 / 4 * self.HEIGHT
        width = self.WIDTH
        height = 1 / 2 * self.HEIGHT
        pygame.draw.rect(self.screen, self.DARK_GRAY, (x, y, width, height))

        pygame.draw.line(self.screen, self.LIGHT_GRAY, (x, y), (x + width, y), 4)
        pygame.draw.line(
            self.screen, self.LIGHT_GRAY, (x, y + height), (x + width, y + height), 4
        )

        text = "[click anywhere to continue]"
        text_surface = self.render_text(text, int(self.WIDTH * 0.032), self.TEXT_COLOR)
        self.blit_text(text_surface, 0.5 * self.WIDTH, 0.65 * self.HEIGHT, "center")
        return

    def draw_rect_lines(
        self,
        color: (int, int, int),
        str_x: int,
        str_y: int,
        end_x: int,
        end_y: int,
        width: int,
    ) -> None:
        pygame.draw.line(self.screen, color, (str_x, str_y), (end_x, str_y), width)
        pygame.draw.line(self.screen, color, (str_x, end_y), (end_x, end_y), width)
        pygame.draw.line(self.screen, color, (str_x, str_y), (str_x, end_y), width)
        pygame.draw.line(self.screen, color, (end_x, str_y), (end_x, end_y), width)
        return

    def run(self) -> None:
        pass
