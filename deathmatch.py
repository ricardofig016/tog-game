import random
from floor_test import FloorTest


class Deathmatch(FloorTest):
    def __init__(self) -> None:
        super().__init__(
            NAME="Deathmatch Test",
            FLOOR="2F/Evankhell's hell",
            GRID_SIZE=10,
            TEAM_SIZE=1,
            BG_IMAGE_PATH=self.get_random_bg_image(),
        )

    def get_random_bg_image(self):
        images = [
            "assets/deathmatch_test1.jpg",
            "assets/deathmatch_test2.jpg",
            "assets/deathmatch_test3.jpg",
        ]
        return images[random.randint(0, len(images) - 1)]
