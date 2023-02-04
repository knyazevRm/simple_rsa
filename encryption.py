class Encryption:
    def __init__(self, text, public_key):
        self.__text = text
        self.__key = public_key
        self.__encryption_text = self.get_encryption_text()

    def get_encryption_text(self):
        return [self.encryption(ord(symbol)) for symbol in self.__text]

    def encryption(self, number):
        return (number ** self.__key.special_arg) % self.__key.general_arg

    @property
    def text(self):
        return self.__text

    @property
    def key(self):
        return self.__key

    @property
    def encryption_text(self):
        return self.__encryption_text