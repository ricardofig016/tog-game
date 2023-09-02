import pygame
from window import Window
from character import Character


class FloorTest(Window):
    def __init__(
        self,
        name: str,
        floor: str,
        grid_size: int,
        team_a_size,
        team_b_size,
        bg_image_path,
    ) -> None:
        self.name = name
        self.floor = floor
        self.grid_size = grid_size
        self.GRID_COLOR = (50, 50, 50)
        self.team_a_size = team_a_size
        self.team_a_size = team_b_size
        caption = f"{self.floor} - {self.name}"
        super().__init__(caption=caption, bg_image_path=bg_image_path)
        self.calc_grid_cell_size()
        self.team_a = []
        self.team_b = []

    def calc_grid_cell_size(self) -> None:
        space = 3 / 5 * self.WIDTH
        self.grid_cell_size = int(space / (self.grid_size + 2))
        return

    def get_info(self) -> str:
        info = self.name
        return info

    def draw_screen_segments(self) -> None:
        pygame.draw.line(
            self.screen,
            self.GRID_COLOR,
            (self.WIDTH * (1 / 5), 0),
            (self.WIDTH * (1 / 5), self.HEIGHT),
            6,
        )
        pygame.draw.line(
            self.screen,
            self.GRID_COLOR,
            (self.WIDTH - self.WIDTH * (1 / 5), 0),
            (self.WIDTH - self.WIDTH * (1 / 5), self.HEIGHT),
            6,
        )
        return

    def draw_grid(self) -> None:
        start_x = int(1 / 5 * self.WIDTH) + self.grid_cell_size
        end_x = start_x + self.grid_cell_size * self.grid_size
        start_y = int((self.HEIGHT - 3 / 5 * self.WIDTH) / 2) + self.grid_cell_size
        end_y = start_y + self.grid_cell_size * self.grid_size

        # vertical lines
        for x in range(start_x, end_x + 1, self.grid_cell_size):
            pygame.draw.line(self.screen, self.GRID_COLOR, (x, start_y), (x, end_y), 4)

        # horizontal lines
        for y in range(start_y, end_y + 1, self.grid_cell_size):
            pygame.draw.line(self.screen, self.GRID_COLOR, (start_x, y), (end_x, y), 4)
        return

    def insert_character(self, id: int, team: str) -> None:
        new_character = Character(id)
        if team.lower() == "a":
            self.team_a.append(new_character)
            print("inserted on team a")
            return
        self.team_b.append(new_character)
        return

    def blit_characters(self) -> None:  # unfinished
        for character in self.team_a:
            profile_img = self.load_and_resize_image(character.profile_img_path, 60, 60)
            self.screen.blit(profile_img, (100, 100))
        for character in self.team_b:
            profile_img = self.load_and_resize_image(
                character.profile_img_path, 100, 100
            )
            self.screen.blit(profile_img, (100, 100))

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.insert_character(1, "a")
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.bg_image, (0, 0))

            self.draw_screen_segments()
            self.draw_grid()

            self.blit_characters()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        return
