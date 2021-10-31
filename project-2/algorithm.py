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
    def mutate(guess, colors=const.COLORS) -> list:
        current_guess = list(guess)
        position = random.randint(0, len(current_guess) - 1)
        new_colors = list(colors)
        bit = current_guess[position]
        new_colors.remove(bit)
        current_guess[position] = random.choice(new_colors)
        return current_guess

    @staticmethod
    def mutate_algorithm(goal, guess, colors=const.COLORS) -> (list, int):
        attempts = 1
        current_guess = list(guess)
        initial_fitness = RandomAlgorithm.fitness(goal, current_guess)
        for i in range(const.LIMIT_MUTATE):
            attempts += 1
            tmp_guess = RandomAlgorithm.mutate(current_guess, colors)
            guess_fitness = RandomAlgorithm.fitness(goal, tmp_guess)
            if tmp_guess == goal:
                return tmp_guess, attempts
            elif guess_fitness > initial_fitness:
                current_guess = tmp_guess
        return current_guess, attempts

    @staticmethod
    def genetic_algorithm_mutate(goal, colors=const.COLORS) -> (list, int):
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
                if is_stagnates and attempts > 1:
                    return (pop[0], attempts) if len(pop) > 0 else ([], attempts)

            # prepare next generation
            mutations = [RandomAlgorithm.mutate(best_evaluations[i % const.POP_BEST], colors) for i in
                         range(const.POP_SIZE - const.POP_BEST)]
            pop = best_evaluations + mutations

    @staticmethod
    def crossover(guess1, guess2) -> (list, list):
        copy_guess1, copy_guess2 = list(guess1), list(guess2)
        if random.uniform(0, 1) < const.PROB_CROSSOVER:
            splitter = random.randint(1, len(guess1) - 2)
            copy_guess1 = guess1[:splitter] + guess2[splitter:]
            copy_guess2 = guess2[:splitter] + guess1[splitter:]
        return copy_guess1, copy_guess2

    @staticmethod
    def genetic_algorithm_crossover(goal, colors=const.COLORS) -> (list, int):
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
                if is_stagnates and attempts > 1:
                    return (pop[0], attempts) if len(pop) > 0 else ([], attempts)

            # prepare next generation
            crossovers = []
            for i in range(0, const.POP_SIZE - const.POP_BEST, 2):
                g1, g2 = RandomAlgorithm.crossover(best_evaluations[i % const.POP_BEST],
                                                   best_evaluations[(i + 1) % const.POP_BEST])
                crossovers.append(g1)
                crossovers.append(g2)
            pop = best_evaluations + crossovers
