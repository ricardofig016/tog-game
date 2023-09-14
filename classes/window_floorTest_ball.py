import random
import os
from classes.window_floorTest import FloorTest


class Ball(FloorTest):
    def __init__(self) -> None:
        super().__init__(
            name="Ball Test",
            floor="1F",
            grid_size=5,
            team_a_size=1,
            team_b_size=2,
            bg_image_path=self.get_random_bg_image(),
            selected_cell=[2, 0],
            prompt="Walk to the Shinue to fight it, destroy the Ball",
            turn="a",
        )
        self.populate_grid()

    def populate_grid(self):
        self.grid[0][2].set_element("boulder")
        self.grid[1][2].set_element("boulder")
        self.grid[3][2].set_element("boulder")
        self.grid[4][2].set_element("boulder")
        self.insert_character(3, "a", 2, 0)
        self.insert_character(6, "b", 2, 2)
        self.insert_character(7, "b", 2, 4)

    def get_random_bg_image(self):
        dir_path = "assets/deathmatch_test"
        images = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                images.append(file_path)
        return images[random.randint(0, len(images) - 1)]

    # moves rak in bams direction
    def make_opponent_turn(self):
        move = self.find_best_move()
        if move:
            self.move_character(move)
            return
        av_moves = self.available_moves(self.selected_cell)
        if av_moves:
            self.move_character(random.choice(av_moves))
            return
        self.flip_turn()
        return

    def find_best_move(self) -> str:
        """
        str: "l", "r", "u", "d"
        """
        bam_coords = self.find_character(3, "a")
        path = ""
        if bam_coords:
            path = self.bfs(self.selected_cell, bam_coords)
        if path:
            return path[0]
        return ""

    def attack(self, attacker: [int, int], defender: [int, int]):
        if (
            self.grid[defender[0]][defender[1]].character.id == 4
            or self.grid[attacker[0]][attacker[1]].character.id == 4
        ):
            self.winner = "a"
            return
        self.winner = "b"
        return
