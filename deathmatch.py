from floor_test import FloorTest


class Deathmatch(FloorTest):
    def __init__(self) -> None:
        super().__init__(
            name="Deathmatch Test",
            grid_size=(10, 10),
            team_size=1,
            bg_image_path="assets/deathmatch_test.jpg",
        )
