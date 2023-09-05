import os
import csv
from classes.window_floorTest_deathmatch import Deathmatch
from classes.player import Player
from classes.character import Character
from classes.cell import Cell
from classes.window_login import Login


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


login = Login()
login.run()

# p = Player("ricardo")
# print(p)

# dm = Deathmatch()
# dm.run()

# print_all_characters()
