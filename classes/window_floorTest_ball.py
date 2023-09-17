import random
import os
from classes.window_tutorial import Tutorial
from classes.window_floorTest import FloorTest


class Ball(FloorTest):
    def __init__(self) -> None:
        super().__init__(
            name="Ball Test",
            floor="1F",
            grid_size=7,
            team_a_size=1,
            team_b_size=2,
            bg_image_path=self.get_random_bg_image(),
            selected_cell=[3, 0],
            prompt="Walk to the Eel to fight it, then pop the Ball",
            turn="a",
        )
        self.populate_grid()

    def populate_grid(self):
        self.grid[0][3].set_element("bars")
        self.grid[1][3].set_element("bars")
        self.grid[2][3].set_element("bars")
        self.grid[4][3].set_element("bars")
        self.grid[5][3].set_element("bars")
        self.grid[6][3].set_element("bars")
        self.insert_character(3, "a", 3, 0)
        self.insert_character(6, "b", 3, 3)
        self.insert_character(7, "b", 3, 6)

    def get_random_bg_image(self):
        dir_path = "assets/test_bgs/ball_test"
        images = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                images.append(file_path)
        return images[random.randint(0, len(images) - 1)]

    def make_opponent_turn(self):
        self.flip_turn()
        return

    def attack(self, attacker: [int, int], defender: [int, int]):
        self.kill_character(defender)
        winner_team = self.check_win()
        if winner_team:
            self.winner = winner_team
        return

    def run(self):
        tut_text = "gosto de panquecas, porque sao docinhas."
        tut = Tutorial(self.bg_image_path, self.caption, tut_text)
        tut.run()
        super().run()
        return
