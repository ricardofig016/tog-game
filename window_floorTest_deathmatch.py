import random
import os
from window_floorTest import FloorTest


class Deathmatch(FloorTest):
    def __init__(self) -> None:
        super().__init__(
            NAME="Deathmatch Test",
            FLOOR="2F/Evankhell's hell",
            GRID_SIZE=12,
            TEAM_SIZE=1,
            BG_IMAGE_PATH=self.get_random_bg_image(),
        )

    def get_random_bg_image(self):
        dir_path = "assets/deathmatch_test"
        images = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                images.append(file_path)
        return images[random.randint(0, len(images) - 1)]
