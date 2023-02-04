class Decryption:
    def __init__(self, text, private_key):
        self.__encryption_text = text
        self.__key = private_key
        self.__decryption_text = self.get_decryption_text()

    def get_decryption_text(self):
        return [self.decryption(symbol) for symbol in self.__encryption_text]

    def decryption(self, number):
        return (number ** self.__key.special_arg) % self.__key.general_arg

    @property
    def encryption_text(self):
        return self.__encryption_text

    @property
    def key(self):
        return self.__key

    @property
    def decryption_text(self):
        return self.__decryption_text