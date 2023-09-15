import os
import csv
from classes.window_login import Login
from classes.player import Player
from classes.window_mainMenu import MainMenu
from classes.character import Character
from classes.cell import Cell
from classes.window_floorTest_ball import Ball
from classes.window_floorTest_deathmatch import Deathmatch


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


def run() -> None:
    login = Login()
    player = login.run()
    if not player:
        return
    main_menu = MainMenu(player)
    main_menu.run()
    return


p = Player("test_p")

main_menu = MainMenu(p)
main_menu.run()
#
#
# dm = Ball()
# dm.run()
#
# print_all_characters()

if __name__ == "__main__":
    # run()
    pass
