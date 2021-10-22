import const
import time


class MasterMind:

    def __init__(self) -> None:
        super().__init__()

    def play(self, goal) -> float:
        start_time = time.time()
        attempts = 0

        return time.time() - start_time, attempts
