from generation_key.key.key import Key


class PublicKey(Key):
    def __init__(self, general_arg, special_arg):
        super().__init__(general_arg, special_arg)