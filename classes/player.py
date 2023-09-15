import os


class Player(object):
    def __init__(self, username: str = None) -> None:
        self.username = username
        self.player_file = os.path.join("data/players", self.username + ".txt")
        if not self.exists():
            self.create()
        self.read_data()
        self.floor = int(self.floor)
        self.test = int(self.test)

    def exists(self) -> bool:
        dir_path = os.path.split(self.player_file)[0]
        for filename in os.listdir(dir_path):
            if filename == os.path.split(self.player_file)[1]:
                return True
        return False

    def create(self) -> None:
        with open(self.player_file, "w") as file:
            file.write("floor:1\n")
            file.write("test:1\n")
        return

    def read_data(self) -> None:
        file_values = []
        with open(self.player_file, "r") as file:
            for line in file:
                file_values.append(line.strip().split(":")[1])
            self.floor, self.test = file_values
        return

    def update_file(self) -> None:
        with open(self.player_file, "r") as file:
            lines = file.readlines()

        lines[0] = f"floor:{self.floor}\n"
        lines[1] = f"test:{self.test}\n"

        with open(self.player_file, "w") as file:
            file.writelines(lines)
        return

    def advance_to_next_test(self) -> None:
        test_order = [(1, 1), (2, 1)]
        current = (self.floor, self.test)
        if current == test_order[-1]:
            return
        self.floor, self.test = test_order[test_order.index(current) + 1]
        self.update_file()
        return

    def delete(self) -> None:
        os.remove(self.player_file)
        return

    def __str__(self) -> str:
        info = ""
        for var_name, var_value in vars(self).items():
            info += f"{var_name}: {var_value}"
            info += "\n"
        return info[:-1]
