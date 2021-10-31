import const
import algorithm as a
import time


class MasterMind:

    final_guess: list
    final_goal: list

    def __init__(self) -> None:
        super().__init__()

    def play(self, goal, algorithm) -> (float, int):
        start_time = time.time()
        guess = None
        self.final_goal = list(goal)
        attempts = 0
        while attempts == 0 or goal != guess:
            self.final_guess = algorithm(guess)
            guess = list(self.final_guess)
            attempts += 1
        return (time.time() - start_time), attempts, self

    def play_mutate(self, goal, guess, colors=const.COLORS) -> (float, int):
        start_time = time.time()
        self.final_goal = list(goal)
        attempts = 1
        if goal != guess:
            self.final_guess, attempts = a.RandomAlgorithm.mutate_algorithm(goal, guess, colors)
        return (time.time() - start_time), attempts, self

    def play_genetic_algorithm_mutate(self, goal, colors=const.COLORS) -> (float, int):
        start_time = time.time()
        self.final_goal = list(goal)
        self.final_guess, attempts = a.RandomAlgorithm.genetic_algorithm_mutate(goal, colors)
        return (time.time() - start_time), attempts, self

    def play_genetic_algorithm_crossover(self, goal, colors=const.COLORS) -> (float, int):
        start_time = time.time()
        self.final_goal = list(goal)
        self.final_guess, attempts = a.RandomAlgorithm.genetic_algorithm_crossover(goal, colors)
        return (time.time() - start_time), attempts, self
