import os
import csv


class Character(object):
    def __init__(self, id) -> None:
        self.read_entry(id, "data/characters/general.csv")
        self.profile_img_path = self.get_profile_img()

    def read_entry(self, line, filepath) -> None:
        with open(filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row_number, row in enumerate(reader):
                if row_number == line:
                    (
                        self.id,
                        self.name,
                        self.arc,
                        self.position,
                        self.floor,
                    ) = row
                    self.id = int(self.id)
                    self.floor = int(self.floor)
                    break
        return

    def get_profile_img(self) -> str:
        dir_path = "assets/character_profiles"
        prefix = f"{self.id}_"
        for filename in os.listdir(dir_path):
            if filename.startswith(prefix):
                return os.path.join(dir_path, filename)

    def __str__(self) -> str:
        info = ""
        for var_name, var_value in vars(self).items():
            info += f"{var_name}: {var_value}"
            info += "\n"
        return info[:-1]
