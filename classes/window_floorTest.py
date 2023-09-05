import pygame
import time
import copy
from collections import deque
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
        self.team_a_selected_preference = None
        self.team_b_selected_preference = None
        self.prompt = prompt
        self.turn = turn
        caption = f"{self.floor} - {self.name}"
        super().__init__(caption=caption, bg_image_path=bg_image_path)
        self.calc_grid_cell_size()
        self.team_a = []
        self.team_b = []
        self.winner = None

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

    def update_selected_cell(self, coords: [int, int]) -> None:
        self.selected_cell = coords
        if self.turn == "a":
            self.team_a_selected_preference = self.selected_cell
        elif self.turn == "b":
            self.team_b_selected_preference = self.selected_cell
        else:
            raise Exception("invalid team")
        return

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

    def update_teams(self):
        self.team_a = []
        self.team_b = []
        for row in self.grid:
            for cell in row:
                if cell.character:
                    if cell.team == "a":
                        self.team_a.append(cell.character)
                    elif cell.team == "b":
                        self.team_b.append(cell.character)
        return

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

    def reset_selected_cell(self) -> None:
        if self.turn == "a" and self.team_a_selected_preference:
            self.selected_cell = self.team_a_selected_preference[:]
            return
        elif self.turn == "b" and self.team_b_selected_preference:
            self.selected_cell = self.team_b_selected_preference[:]
            return

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = self.grid[i][j]
                if cell.character and cell.team == self.turn:
                    self.selected_cell = [i, j]
                    return
        raise Exception("team is empty")
        return

    def move_character(self, key: str) -> None:
        """
        valid keys: "l", "r", "u", "d"
        """
        h_mult = 0
        v_mult = 0
        sel_cell = self.grid[self.selected_cell[0]][self.selected_cell[1]]
        if key == "l" and self.selected_cell[1] != 0:
            h_mult = -1
        if key == "r" and self.selected_cell[1] != self.grid_size - 1:
            h_mult = +1
        if key == "u" and self.selected_cell[0] != 0:
            v_mult = -1
        if key == "d" and self.selected_cell[0] != self.grid_size - 1:
            v_mult = +1

        if not self.grid[self.selected_cell[0] + v_mult][
            self.selected_cell[1] + h_mult
        ].is_free():
            return

        self.grid[self.selected_cell[0] + v_mult][
            self.selected_cell[1] + h_mult
        ] = copy.deepcopy(sel_cell)
        sel_cell.clear_character()
        self.update_selected_cell(
            [self.selected_cell[0] + v_mult, self.selected_cell[1] + h_mult]
        )

        self.check_interactions(self.selected_cell)
        self.flip_turn()
        return

    def check_interactions(self, coords) -> None:
        x, y = coords
        if x + 1 < self.grid_size:
            self.interact(x + 1, y)
        if x - 1 >= 0:
            self.interact(x - 1, y)
        if y + 1 < self.grid_size:
            self.interact(x, y + 1)
        if y - 1 >= 0:
            self.interact(x, y - 1)
        return

    def interact(self, border_x, border_y) -> None:
        sel_x, sel_y = self.selected_cell

        # there is a character on the border
        if self.grid[border_x][border_y].character:
            # same team
            if self.grid[border_x][border_y].team == self.grid[sel_x][sel_y].team:
                pass
            # if team is neutral it changes to selected character's team
            elif self.grid[border_x][border_y].team == "n":
                if not self.is_team_full(self.grid[sel_x][sel_y].team):
                    self.grid[border_x][border_y].set_team(self.grid[sel_x][sel_y].team)
                    self.update_teams()
            # opposite teams
            else:
                self.attack(self.selected_cell, [border_x, border_y])
        return

    def is_team_full(self, team: str) -> bool:
        if team == "a":
            return len(self.team_a) >= self.team_a_size
        if team == "b":
            return len(self.team_b) >= self.team_b_size
        raise Exception("invalid team")

    def flip_turn(self) -> None:
        if self.turn == "a":
            self.turn = "b"
        elif self.turn == "b":
            self.turn = "a"
        else:
            raise Exception("invalid team")
        self.reset_selected_cell()
        return

    def make_opponent_turn(self):
        pass

    def find_character(self, id: int = None, team: str = None) -> [int, int]:
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = self.grid[i][j]
                if cell.character:
                    if not id and not team:
                        return [i, j]
                    if not id and cell.team == team:
                        return [i, j]
                    if cell.character.id == id and not team:
                        return [i, j]
                    if cell.character.id == id and cell.team == team:
                        return [i, j]
        return

    def available_moves(self, coords) -> str:
        """
        returns a str between "" and "lrup"
        """
        x, y = coords
        moves = ""
        if y - 1 >= 0 and self.grid[x][y - 1].is_free():
            moves += "l"
        if y + 1 < self.grid_size and self.grid[x][y + 1].is_free():
            moves += "r"
        if x - 1 >= 0 and self.grid[x - 1][y].is_free():
            moves += "u"
        if x + 1 < self.grid_size and self.grid[x + 1][y].is_free():
            moves += "d"
        return moves

    def manhattan_distance(self, a: [int, int], b: [int, int]) -> bool:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def bfs(self, start: [int, int], target: [int, int]) -> str:
        """
        Args:
            start ([int,int]): coords of root node
            target ([int,int]): coords of target node

        Returns:
            str: path to target using "l", "r", "u", "d"
        """
        q = deque()
        q.append([start, ""])
        vis = [[False for i in range(self.grid_size)] for j in range(self.grid_size)]
        while len(q) > 0:
            cell = q.popleft()

            if self.manhattan_distance(cell[0], target) <= 1:
                return cell[1]  # path

            av_moves = self.available_moves(cell[0])
            x, y = cell[0]
            for key in av_moves:
                if key == "l":
                    adj_x = x
                    adj_y = y - 1
                if key == "r":
                    adj_x = x
                    adj_y = y + 1
                if key == "u":
                    adj_x = x - 1
                    adj_y = y
                if key == "d":
                    adj_x = x + 1
                    adj_y = y

                if not (vis[adj_x][adj_y]):
                    q.append([[adj_x, adj_y], cell[1] + key])
                    vis[adj_x][adj_y] = True
        return ""

    def attack(self, attacker: [int, int], defender: [int, int]):
        print(attacker, defender)
        return

    def blit_winner(self):
        x = 0
        y = 1 / 4 * self.HEIGHT
        width = self.WIDTH
        height = 1 / 2 * self.HEIGHT
        pygame.draw.rect(self.screen, self.GRID_COLOR, (x, y, width, height))

        pygame.draw.line(
            self.screen,
            self.LIGHT_GRAY,
            (0, 1 / 4 * self.HEIGHT),
            (self.WIDTH, 1 / 4 * self.HEIGHT),
            4,
        )
        pygame.draw.line(
            self.screen,
            self.LIGHT_GRAY,
            (0, 3 / 4 * self.HEIGHT),
            (self.WIDTH, 3 / 4 * self.HEIGHT),
            4,
        )

        if self.winner == "a":
            text = "YOU WIN"
            color = self.GREEN
        elif self.winner == "b":
            text = "YOU LOSE"
            color = self.RED
        else:
            raise Exception(f"{self.winner} is not a valid winner")
        text_surface = self.render_text(text, int(self.WIDTH * 0.2), color)
        self.blit_text(text_surface, 0.5 * self.WIDTH, 0.5 * self.HEIGHT, "center")

        text = "[click anywhere to continue]"
        text_surface = self.render_text(text, int(self.WIDTH * 0.032), self.TEXT_COLOR)
        self.blit_text(text_surface, 0.5 * self.WIDTH, 0.65 * self.HEIGHT, "center")
        return

    def winner_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.bg_image, (0, 0))
            self.draw_grid()
            self.blit_teams()
            self.blit_winner()

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        return

    def run(self) -> None:
        running = True
        while running:
            # self.mouse_pos = pygame.mouse.get_pos()

            if self.turn == "b":
                time.sleep(self.SLEEP_TIME)
                self.make_opponent_turn()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if self.turn == "a":
                        if event.key == pygame.K_TAB:
                            self.tab_selected_cell()
                        if event.key == pygame.K_LEFT:
                            self.move_character("l")
                        if event.key == pygame.K_RIGHT:
                            self.move_character("r")
                        if event.key == pygame.K_UP:
                            self.move_character("u")
                        if event.key == pygame.K_DOWN:
                            self.move_character("d")
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.bg_image, (0, 0))
            self.draw_grid()
            self.blit_teams()

            pygame.display.update()
            self.clock.tick(60)

            if self.winner:
                time.sleep(self.SLEEP_TIME)
                self.winner_loop()
                running = False

        pygame.quit()
        return
