class Key:
    def __init__(self, general_arg, special_arg):
        self.__general_arg = general_arg
        self.__special_arg = special_arg

    def __repr__(self):
        return f"{self.__special_arg} {self.__general_arg}"

    @property
    def general_arg(self):
        return self.__general_arg

    @property
    def special_arg(self):
        return self.__special_arg