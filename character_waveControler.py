import csv
from character import Character


class WaveControler(Character):
    def __init__(self, id) -> None:
        super().__init__()
        self.read_entry(id, "data/characters/wave_controlers.csv")

    def read_entry(self, line, filepath) -> None:
        with open(filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row_number, row in enumerate(reader):
                if row_number == line:
                    self.ID, self.NAME, self.SOBRIQUET = row
                    break
        return
