import pygame
from window import Window


class FloorTest(Window):
    def __init__(self, NAME, FLOOR, GRID_SIZE, TEAM_SIZE, BG_IMAGE_PATH) -> None:
        self.NAME = NAME
        self.FLOOR = FLOOR
        self.GRID_SIZE = GRID_SIZE
        self.GRID_CELL_SIZE = 60
        self.GRID_COLOR = (100, 100, 100)
        self.TEAM_SIZE = TEAM_SIZE
        CAPTION = f"{self.FLOOR} - {self.NAME}"
        super().__init__(CAPTION=CAPTION, BG_IMAGE_PATH=BG_IMAGE_PATH)

    def get_info(self) -> str:
        info = self.name
        return info

    def draw_screen_segments(self) -> None:
        pygame.draw.line(
            self.screen,
            self.GRID_COLOR,
            (self.WIDTH * (1 / 5), 0),
            (self.WIDTH * (1 / 5), self.HEIGHT),
            5,
        )
        pygame.draw.line(
            self.screen,
            self.GRID_COLOR,
            (self.WIDTH - self.WIDTH * (1 / 5), 0),
            (self.WIDTH - self.WIDTH * (1 / 5), self.HEIGHT),
            5,
        )
        self.draw_grid()
        return

    def draw_grid(self) -> None:
        start_x = int(1 / 5 * self.WIDTH) + self.GRID_CELL_SIZE
        end_x = int(4 / 5 * self.WIDTH) - self.GRID_CELL_SIZE
        start_y = int((self.HEIGHT - 3 / 5 * self.WIDTH) / 2) + self.GRID_CELL_SIZE
        end_y = (
            int(self.HEIGHT - (self.HEIGHT - 3 / 5 * self.WIDTH) / 2)
            - self.GRID_CELL_SIZE
        )

        # vertical lines
        for x in range(start_x, end_x + 1, self.GRID_CELL_SIZE):
            pygame.draw.line(self.screen, self.GRID_COLOR, (x, start_y), (x, end_y), 2)

        # horizontal lines
        for y in range(start_y, end_y + 1, self.GRID_CELL_SIZE):
            pygame.draw.line(self.screen, self.GRID_COLOR, (start_x, y), (end_x, y), 2)
        return
