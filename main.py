import os
import csv
from window_floorTest_deathmatch import Deathmatch
from character_waveControler import WaveControler


def print_all_characters():
    dir_path = "data/characters"
    characters = []
    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row_index, row in enumerate(reader):
                if row_index != 0:
                    characters.append(row)

    characters = sorted(characters, key=lambda x: int(x[0]))

    for character in characters:
        print(character)


dm = Deathmatch()
dm.run()

bam = WaveControler(1)
print(bam.get_info())

print_all_characters()
