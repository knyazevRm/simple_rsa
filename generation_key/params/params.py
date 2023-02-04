from generation_key import utils


class Params:
    def __init__(self):
        self.__p, self.__q = utils.generation_param_p_and_q()
        self.__n = self.get_n()
        self.__argument = (self.__p - 1) * (self.__q - 1)
        self.__d = self.get_d()
        self.__e = self.get_e()

    def get_n(self):
        return self.__p * self.__q

    def get_d(self):
        return utils.get_random_d(self.__argument)

    def get_e(self):
        return utils.get_random_e(self.__n, self.__d, self.__argument)

    @property
    def p(self):
        return self.__p

    @property
    def q(self):
        return self.__q

    @property
    def n(self):
        return self.__n

    @property
    def d(self):
        return self.__d

    @property
    def e(self):
        return self.__e

    @property
    def argument(self):
        return self.__argument