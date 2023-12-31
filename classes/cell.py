import os
import random
from classes.character import Character


class Cell(object):
    def __init__(self) -> None:
        self.character = None
        self.team = None
        self.elements = ["boulder", "bars"]
        self.element = ""
        self.img = self.get_img()

    def set_element(self, elem: str) -> None:
        if elem == "" or elem in self.elements:
            self.element = elem
            self.img = self.get_img()
        return

    def set_team(self, team: str) -> None:
        self.team = team
        self.img = self.get_img()
        return

    def get_img(self) -> str:
        if self.character:
            return self.character.profile_img_path
        if self.element == "boulder":
            return self.get_random_boulder()
        if self.element == "bars":
            return "assets/cell_elements/bars.jpg"
        return "assets/white.png"

    def get_random_boulder(self) -> str:
        dir_path = "assets/cell_elements/boulders"
        images = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                images.append(file_path)
        return images[random.randint(0, len(images) - 1)]

    def is_free(self):
        if self.character or self.element in self.elements:
            return False
        return True

    def insert_character(self, character: Character, team: str) -> bool:
        if self.character or self.element in self.elements:
            return False
        self.character = character
        self.team = team
        self.img = self.get_img()
        return True

    def clear_character(self) -> None:
        self.character = None
        self.team = None
        self.img = self.get_img()
        return
