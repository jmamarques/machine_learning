import numpy as np

import iml.environment as env
import iml.const as const


class QLearning:
    """Exercise 2 q-learning"""
    guesses: [{}]
    alpha: float
    discount: float

    def __init__(self, guesses=None, alpha=0.7, discount=0.99) -> None:
        super().__init__()
        self.guesses = self.__initialize_guesses(const.WORLD_HEIGHT * const.WORLD_WIDTH,
                                                 const.ACTIONS) if guesses is None else guesses
        self.alpha = alpha
        self.discount = discount

    @staticmethod
    def __initialize_guesses(size, actions) -> [{}]:
        """create initial matrix for all actions - default value 0.0"""
        res: [{}] = []
        for i in range(size):
            dict = {}
            for action in actions:
                dict[action] = 0.0
            res.append(dict)

        return res

    def algorithm_q_learning(self, state, action, next_state):
        # get current guess
        q_state: float = self.guesses[state][action]
        # calculate maximum guesses for all actions
        q_next_state_max: float = np.max(list(self.guesses[next_state].values()))
        # new guess for previous state
        q_new_state: float = (1.0 - self.alpha) * q_state + self.alpha * (
                    env.reward(next_state) + self.discount * q_next_state_max)

        self.guesses[state][action] = q_new_state

    """
    2-
    Can you now tell which is the best sequence of actions using the information on Q? 
    And the best action from any given state?
    A: 
    """

v = QLearning()
v.algorithm_q_learning(1, const.DOWN, 11)
print(v.guesses)
