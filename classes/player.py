import os


class Player(object):
    def __init__(self, username: str = None) -> None:
        self.username = username
        self.player_file = os.path.join("data/players", self.username + ".txt")
        if self.exists():
            self.read_data()
        else:
            self.create()

    def exists(self) -> bool:
        dir_path = os.path.split(self.player_file)[0]
        for filename in os.listdir(dir_path):
            if filename == os.path.split(self.player_file)[1]:
                return True
        return False

    def create(self) -> None:
        with open(self.player_file, "w") as file:
            file.write(f"username:{self.username}\n")
        return

    def read_data(self) -> None:
        with open(self.player_file, "r") as file:
            pass
        return

    def delete(self) -> None:
        os.remove(self.player_file)
        return
