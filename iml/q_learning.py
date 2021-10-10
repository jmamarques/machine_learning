import numpy as np

import iml.const as const
import iml.environment as env


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

    @staticmethod
    def matrix_guesses(guesses: [{}]) -> [[]]:
        res: [[]] = []
        for guess in guesses:
            res.append(list(guess.values()))
        return res

    def algorithm_q_learning(self, state, action, next_state) -> None:
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

    def run_episode(self, actions=env.random_action, execution_times=20000) -> [(int, int, [[[]]])]:
        """:return  Array of(
                    0: points - total rewards
                    1: numbSteps - array with number os steps
                    2: q-table
        """
        # initial context
        stats: [(int, [], [[[]]])] = []
        state = 0
        points = 0
        steps = 0
        numb_steps = []
        # execution_times attempts
        for i in range(execution_times):
            # apply random action
            action = actions()
            pre_state = state
            state = env.next_state(pre_state, action)
            steps += 1
            # end episode - back to home
            current_state, current_reward, is_final_state = env.end_episode(state)
            # count many times that reach the reward
            if is_final_state:
                numb_steps.append(steps)
                steps = 0
            # update q learning table
            # arguments: state before the execution of next step, action choose, next state
            self.algorithm_q_learning(pre_state, action, state)
            # update variables
            state = current_state
            points += current_reward
            self.__save_statistics(i, (points, numb_steps), stats)
        return points, numb_steps,

    def __save_statistics(self, current_index, current_situation, accumulator: [(int, [], [[[]]])]) -> None:
        """save statistics on accumulator for next analysis"""
        if current_index == 99 or current_index == 199 or current_index == 499 or current_index == 599 \
                or current_index == 799 or current_index == 899 or current_index == 999 or current_index == 2499 \
                or current_index == 4999 or current_index == 7499 or current_index == 9999 \
                or current_index == 12499 or current_index == 14999 or current_index == 17499 \
                or current_index == 19999:
            points, numb_steps = current_situation
            accumulator.append((points, numb_steps, QLearning.matrix_guesses(self.guesses)))


v = QLearning()
v.run_episode()
print("Print:")
print(np.matrix(QLearning.matrix_guesses(v.guesses)))
print(v.guesses)
