import const
import random
import copy


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
        return len(goal) * const.POINTS - RandomAlgorithm.evaluate(goal, guess)

    @staticmethod
    def mutate(goal, guess, colors=const.COLORS) -> list:
        current_guess = list(guess)
        initial_fitness = RandomAlgorithm.fitness(goal, current_guess)
        for i in range(const.LIMIT_MUTATE):
            position = random.randint(0, len(current_guess) - 1)
            new_colors = list(colors)
            new_colors.remove(current_guess[position])
            current_guess[position] = random.choice(new_colors)
            guess_fitness = RandomAlgorithm.fitness(goal, current_guess)
            if guess_fitness > initial_fitness or current_guess == goal:
                return current_guess
        return guess

