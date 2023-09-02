class Character(object):
    def __init__(self) -> None:
        pass

    def get_info(self):
        info = ""
        for var_name, var_value in vars(self).items():
            info += f"{var_name}: {var_value}"
            info += "\n"
        return info[:-1]
