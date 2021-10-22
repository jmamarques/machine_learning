import const
import random


class RandomAlgorithm:

    @staticmethod
    def random_bit(colors=const.COLORS):
        return random.choice(colors)
