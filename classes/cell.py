import os
import random
from classes.character import Character


class Cell(object):
    def __init__(self) -> None:
        self.character = None
        self.element = ""
        self.img = self.get_img()

    def set_element(self, elem: str) -> None:
        if elem in ["", "boulder"]:
            self.element = elem
            self.img = self.get_img()

    def get_img(self) -> str:
        if self.character:
            return self.character.profile_img_path
        if self.element == "boulder":
            return self.get_random_boulder()
        return "assets/cell_elements/none.png"

    def get_random_boulder(self) -> str:
        dir_path = "assets/cell_elements/boulders"
        images = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                images.append(file_path)
        return images[random.randint(0, len(images) - 1)]

    def insert_character(self, character: Character) -> bool:
        if self.character or self.element in ["boulder"]:
            return False
        self.character = character
        self.img = self.get_img()
        return True