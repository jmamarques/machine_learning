import const
import algorithm as a
import time


class MasterMind:

    def __init__(self) -> None:
        super().__init__()

    def play(self, goal, algorithm) -> (float, int):
        start_time = time.time()
        attempts = 1
        guess = algorithm()
        while goal != guess:
            guess = algorithm()
            attempts += 1
        return (time.time() - start_time), attempts


aa = [1]
b = [1,2]
print( aa == b)
ab = MasterMind()
bb = lambda: a.RandomAlgorithm.random_bit_pattern(64)
print (ab.play(a.RandomAlgorithm.random_bit_pattern(64), bb))
