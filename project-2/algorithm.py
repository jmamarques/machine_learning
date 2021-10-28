import const
import random


class RandomAlgorithm:

    @staticmethod
    def random_bit(colors=const.COLORS):
        return random.choice(colors)

    @staticmethod
    def random_bit_pattern(size, colors=const.COLORS) -> list:
        res = []
        for i in range(size):
            res.append(RandomAlgorithm.random_bit(colors))
        return res

    @staticmethod
    def evaluate(goal, guess) -> int:
        res = 0
        if len(goal) != len(guess):
            raise ValueError("Arrays mismatch - evaluate function")
        for i in range(len(goal)):
            if goal[i] != guess[i]:
                res += const.POINTS
        return res

    @staticmethod
    def fitness(goal, guess) -> int:
        return len(goal) * const.POINTS - const.POINTS * RandomAlgorithm.evaluate(goal, guess)
