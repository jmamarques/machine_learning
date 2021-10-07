import numpy as np

import iml.environment as env
import iml.const as const


class QLearning:
    """Exercise 2 q-learning"""
    guesses: [[]]
    alpha: float
    discount: float

    def __init__(self, guesses=None, alpha=0.7, discount=0.99) -> None:
        super().__init__()
        self.guesses = np.zeros((const.WORLD_HEIGHT, const.WORLD_WIDTH)) if guesses is None else guesses
        self.alpha = alpha
        self.discount = discount


    def algorithm_q_learning(self):

