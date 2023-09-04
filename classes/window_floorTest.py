import pygame
import copy
from classes.window import Window
from classes.character import Character
from classes.cell import Cell
from classes.pygameButton import PygameButton


class FloorTest(Window):
    def __init__(
        self,
        name: str,
        floor: str,
        grid_size: int,
        team_a_size: int,
        team_b_size: int,
        bg_image_path: str,
        selected_cell: [int, int],
        prompt: str = None,
        turn: str = "a",
    ) -> None:
        self.name = name
        self.floor = floor
        self.grid_size = grid_size
        self.create_grid()
        self.GRID_COLOR = self.DARK_GRAY
        self.SELECTED_COLOR = self.YELLOW
        self.team_a_size = team_a_size
        self.team_b_size = team_b_size
        self.selected_cell = selected_cell
        self.prompt = prompt
        self.turn = turn
        caption = f"{self.floor} - {self.name}"
        super().__init__(caption=caption, bg_image_path=bg_image_path)
        self.calc_grid_cell_size()
        self.team_a = []
        self.team_b = []

    def create_grid(self) -> None:
        self.grid = []
        for i in range(self.grid_size):
            self.grid.append([])
            for j in range(self.grid_size):
                c = Cell()
                self.grid[i].append(c)

    def calc_grid_cell_size(self) -> None:
        space = 3 / 5 * self.WIDTH
        self.grid_cell_size = int(space / (self.grid_size + 2))
        return

    def get_info(self) -> str:
        info = self.name
        return info

    def draw_grid(self) -> None:
        start_x = int(1 / 5 * self.WIDTH) + self.grid_cell_size
        end_x = start_x + self.grid_cell_size * self.grid_size
        start_y = int((self.HEIGHT - 3 / 5 * self.WIDTH) / 2) + self.grid_cell_size
        end_y = start_y + self.grid_cell_size * self.grid_size

        self.starting_cell_coords = (
            int(start_x),
            int(start_y),
        )

        self.blit_grid_elements()

        # vertical lines
        for x in range(start_x, end_x + 1, self.grid_cell_size):
            pygame.draw.line(self.screen, self.GRID_COLOR, (x, start_y), (x, end_y), 4)

        # horizontal lines
        for y in range(start_y, end_y + 1, self.grid_cell_size):
            pygame.draw.line(self.screen, self.GRID_COLOR, (start_x, y), (end_x, y), 4)

        self.draw_selected_square()
        return

    def draw_selected_square(self):
        start_x = (
            self.starting_cell_coords[0] + self.selected_cell[1] * self.grid_cell_size
        )
        start_y = (
            self.starting_cell_coords[1] + self.selected_cell[0] * self.grid_cell_size
        )
        end_x = (
            self.starting_cell_coords[0]
            + self.selected_cell[1] * self.grid_cell_size
            + self.grid_cell_size
        )
        end_y = (
            self.starting_cell_coords[1]
            + self.selected_cell[0] * self.grid_cell_size
            + self.grid_cell_size
        )

        color = self.SELECTED_COLOR

        pygame.draw.line(self.screen, color, (start_x, start_y), (end_x, start_y), 4)
        pygame.draw.line(self.screen, color, (start_x, end_y), (end_x, end_y), 4)
        pygame.draw.line(self.screen, color, (start_x, start_y), (start_x, end_y), 4)
        pygame.draw.line(self.screen, color, (end_x, start_y), (end_x, end_y), 4)

    def blit_grid_elements(self):
        for i in range(self.grid_size):
            row = self.grid[i]
            for j in range(self.grid_size):
                element_path = row[j].img
                img_size = self.grid_cell_size
                img = self.load_and_resize_image(element_path, img_size, img_size)
                coords = (
                    self.starting_cell_coords[0] + j * self.grid_cell_size,
                    self.starting_cell_coords[1] + i * self.grid_cell_size,
                )
                self.screen.blit(img, coords)

    def insert_character(self, id: int, team: str, x: int, y: int) -> None:
        new_character = Character(id)
        if team.lower() == "a":
            if len(self.team_a) < self.team_a_size and self.grid[x][y].insert_character(
                new_character, team
            ):
                self.team_a.append(new_character)
                self.grid[x][y]
            return

        if team.lower() == "b":
            if len(self.team_b) < self.team_b_size and self.grid[x][y].insert_character(
                new_character, team
            ):
                self.team_b.append(new_character)
            return

        # neutral character
        self.grid[x][y].insert_character(new_character, team)

    def blit_teams(self) -> None:
        self.blit_team_bg()
        if self.prompt:
            self.blit_prompt()
        # Team A
        text_surface = self.render_text(
            "Team A", int(self.WIDTH * 0.032), self.TEXT_COLOR
        )
        self.blit_text(
            text_surface, 1 / 10 * self.WIDTH, 1.5 / 8 * self.HEIGHT, "center"
        )

        # Team B
        text_surface = self.render_text(
            "Team B", int(self.WIDTH * 0.032), self.TEXT_COLOR
        )
        self.blit_text(
            text_surface, 9 / 10 * self.WIDTH, 1.5 / 8 * self.HEIGHT, "center"
        )

        self.blit_character_profile_images()
        self.blit_character_info()
        return

    def blit_team_bg(self):
        x = 0
        y = 1 / 8 * self.HEIGHT
        width = 1 / 5 * self.WIDTH
        height = (self.team_a_size + 1) / 8 * self.HEIGHT
        pygame.draw.rect(self.screen, self.GRID_COLOR, (x, y, width, height))

        x = self.WIDTH - width
        height = (self.team_b_size + 1) / 8 * self.HEIGHT
        pygame.draw.rect(self.screen, self.GRID_COLOR, (x, y, width, height))

    def blit_prompt(self):
        x = 1 / 5 * self.WIDTH
        y = 19 / 20 * self.HEIGHT
        width = 3 / 5 * self.WIDTH
        height = 1 / 10 * self.HEIGHT
        pygame.draw.rect(self.screen, self.GRID_COLOR, (x, y, width, height))

        prompt_surface = self.render_text(
            self.prompt, int(self.WIDTH * 0.02), self.TEXT_COLOR
        )
        self.blit_text(
            prompt_surface, 0.5 * self.WIDTH, 39 / 40 * self.HEIGHT, "center"
        )

    def blit_character_profile_images(self) -> None:
        for i in range(len(self.team_a)):
            character = self.team_a[i]
            img_size = 1 / 20 * self.WIDTH
            profile_img = self.load_and_resize_image(
                character.profile_img_path, img_size, img_size
            )
            self.screen.blit(
                profile_img, (1 / 120 * self.WIDTH, 1 / 8 * (i + 2) * self.HEIGHT)
            )

        for i in range(len(self.team_b)):
            character = self.team_b[i]
            img_size = 1 / 20 * self.WIDTH
            profile_img = self.load_and_resize_image(
                character.profile_img_path, img_size, img_size
            )
            self.screen.blit(
                profile_img,
                (119 / 120 * self.WIDTH - img_size, 1 / 8 * (i + 2) * self.HEIGHT),
            )
        return

    def blit_character_info(self):
        for i in range(len(self.team_a)):
            character = self.team_a[i]
            text_surface = self.render_text(
                character.name, int(self.WIDTH * 0.02), self.TEXT_COLOR
            )
            self.blit_text(
                text_surface, 1 / 15 * self.WIDTH, 1 / 8 * (i + 2) * self.HEIGHT
            )
        for i in range(len(self.team_b)):
            character = self.team_b[i]
            text_surface = self.render_text(
                character.name, int(self.WIDTH * 0.02), self.TEXT_COLOR
            )
            self.blit_text(
                text_surface, 97 / 120 * self.WIDTH, 1 / 8 * (i + 2) * self.HEIGHT
            )

    def tab_selected_cell(self) -> None:
        valid_coords = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = self.grid[i][j]
                if cell.character and cell.team == "a":
                    valid_coords.append([i, j])
        index = valid_coords.index(self.selected_cell)
        if index == len(valid_coords) - 1:
            self.selected_cell = valid_coords[0]
            return
        self.selected_cell = valid_coords[index + 1]
        return

    def move_character(self, key: str) -> None:
        h_mult = 0
        v_mult = 0
        sel_cell = self.grid[self.selected_cell[0]][self.selected_cell[1]]
        if key == "left" and self.selected_cell[1] != 0:
            h_mult = -1
        if key == "right" and self.selected_cell[1] != self.grid_size - 1:
            h_mult = +1
        if key == "up" and self.selected_cell[0] != 0:
            v_mult = -1
        if key == "down" and self.selected_cell[0] != self.grid_size - 1:
            v_mult = +1

        if not self.grid[self.selected_cell[0] + v_mult][
            self.selected_cell[1] + h_mult
        ].is_free():
            return

        self.grid[self.selected_cell[0] + v_mult][
            self.selected_cell[1] + h_mult
        ] = copy.deepcopy(sel_cell)
        sel_cell.clear_character()
        self.selected_cell = [
            self.selected_cell[0] + v_mult,
            self.selected_cell[1] + h_mult,
        ]
        return

    def run(self) -> None:
        running = True
        while running:
            self.mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.tab_selected_cell()
                    if event.key == pygame.K_LEFT:
                        self.move_character("left")
                    if event.key == pygame.K_RIGHT:
                        self.move_character("right")
                    if event.key == pygame.K_UP:
                        self.move_character("up")
                    if event.key == pygame.K_DOWN:
                        self.move_character("down")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass  #####################################
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.bg_image, (0, 0))
            self.draw_grid()
            self.blit_teams()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        return
