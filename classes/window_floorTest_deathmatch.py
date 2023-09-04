import random
import os
from classes.window_floorTest import FloorTest


class Deathmatch(FloorTest):
    def __init__(self) -> None:
        super().__init__(
            name="Deathmatch Test",
            floor="2F",
            grid_size=5,
            team_a_size=2,
            team_b_size=1,
            bg_image_path=self.get_random_bg_image(),
            selected_cell=[4, 0],
            prompt="Team up with Khun and defeat Rak",
            turn="a",
        )
        self.populate_grid()

    def populate_grid(self):
        self.grid[0][2].set_element("boulder")
        self.grid[1][3].set_element("boulder")
        self.grid[2][3].set_element("boulder")
        self.insert_character(3, "a", 4, 0)
        self.insert_character(4, "a", 1, 1)  # change to "a"
        self.insert_character(5, "b", 0, 4)

    def get_random_bg_image(self):
        dir_path = "assets/deathmatch_test"
        images = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                images.append(file_path)
        return images[random.randint(0, len(images) - 1)]
