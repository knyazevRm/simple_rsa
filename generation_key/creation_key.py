import generation_key.params.params as prm
from generation_key.key.public import PublicKey
from generation_key.key.private import PrivateKey


class CreationKeys:
    def __init__(self):
        self.__param = prm.Params()
        self.__public_key = PublicKey(self.__param.n, self.__param.e)
        self.__private_key = PrivateKey(self.__param.n, self.__param.d)

    @property
    def public_key(self):
        return self.__public_key

    @property
    def private_key(self):
        return self.__private_key

    def get_keys(self):
        return self.__public_key, self.__private_key
