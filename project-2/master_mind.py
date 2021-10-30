import const
import algorithm as a
import time


class MasterMind:

    def __init__(self) -> None:
        super().__init__()

    def play(self, goal, algorithm, guess) -> (float, int):
        start_time = time.time()
        attempts = 1
        while goal != guess:
            guess = algorithm(guess)
            attempts += 1
        return (time.time() - start_time), attempts
