import random
import os
from window_floorTest import FloorTest


class Deathmatch(FloorTest):
    def __init__(self) -> None:
        super().__init__(
            name="Deathmatch Test",
            floor="2F/Evankhell's hell",
            grid_size=12,
            team_a_size=1,
            team_b_size=1,
            bg_image_path=self.get_random_bg_image(),
        )

    def get_random_bg_image(self):
        dir_path = "assets/deathmatch_test"
        images = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                images.append(file_path)
        return images[random.randint(0, len(images) - 1)]
