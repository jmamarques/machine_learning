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
            bit = current_guess[position]
            new_colors.remove(bit)
            current_guess[position] = random.choice(new_colors)
            guess_fitness = RandomAlgorithm.fitness(goal, current_guess)
            if guess_fitness > initial_fitness or current_guess == goal:
                return current_guess
            else:
                current_guess[position] = bit
        return guess

    @staticmethod
    def genetic_algorithm(goal, colors=const.COLORS) -> (list, int):
        attempts = 0
        pop = [RandomAlgorithm.random_bit_pattern(len(goal)) for _ in range(const.POP_SIZE)]
        while True:
            # pop evaluation
            evaluations = [(RandomAlgorithm.fitness(goal, pop[i]), i) for i in range(const.POP_SIZE)]
            evaluations.sort(key=lambda v: v[0], reverse=True)
            best_evaluations = [pop[val[1]] for val in evaluations[0:const.POP_BEST]]
            # increase number of repetitions
            attempts += 1
            if best_evaluations[0] == goal:
                return best_evaluations[0], attempts
            else:
                is_stagnates = True
                if len(pop) > 0:
                    initial_guess = pop[0]
                    for guess in pop:
                        if guess != initial_guess:
                            is_stagnates = False
                            break
                if is_stagnates:
                    return pop[0] if len(pop) > 0 else None

            # prepare next generation
            mutations = [RandomAlgorithm.mutate(goal, best_evaluations[i % const.POP_BEST], colors) for i in
                         range(const.POP_SIZE - const.POP_BEST)]
            pop = best_evaluations + mutations


RandomAlgorithm.genetic_algorithm([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
