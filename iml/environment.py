import iml.const as const
import random

from iml.statistics_base import BaseStatistics

"""This is stateless"""


def next_state(state, action):
    """ requires state belongs to world const.INITIAL <= state <= const.FINAL
        :return next state when we apply an action"""
    if not(const.INITIAL <= state <= const.FINAL):
        raise ValueError('Invalid state')
    move = state
    if action == const.UP:
        next_move = state - const.MOVE_UP_DOWN
        if not (next_move < const.LIMIT_U):
            move = next_move
    elif action == const.DOWN:
        next_move = state + const.MOVE_UP_DOWN
        if not (next_move > const.LIMIT_D):
            move = next_move
    elif action == const.RIGHT:
        if state % 10 != const.LIMIT_R:
            move = state + const.MOVE_RIGHT_LEFT
    elif action == const.LEFT:
        if state % 10 != const.LIMIT_L:
            move = state - const.MOVE_RIGHT_LEFT
    else:
        raise ValueError('Invalid action')
    return move


def reward(state):
    """:return points for that state"""
    return const.NO_REWARD if not is_final_state(state) else const.REWARD


def is_final_state(state):
    """:return True if the state is equals to goal point defined on const.GOAL"""
    return state == const.GOAL


def random_action():
    """:return random action present on const.ACTIONS (up down left right)"""
    return random.choice(const.ACTIONS)


def end_episode(state):
    """ :return state, reward, was final state """
    return const.INITIAL if is_final_state(state) else state, reward(state), is_final_state(state)


def run_episode(actions=random_action, execution_times=1000):
    """ execute execution_times the episode
        :return rewards, list of steps done for reach each goal"""
    # initial context
    state = 0
    points = 0
    steps = 0
    numb_steps = []
    # execution_times attempts
    for i in range(execution_times):
        # apply random action
        state = next_state(state, actions())
        steps += 1
        # end episode - back to home
        progress = end_episode(state)
        # count many times that reach the reward
        if progress[2]:
            numb_steps.append(steps)
            steps = 0
        state = progress[0]
        points += progress[1]
    return points, numb_steps


def run_statistics():
    """ run 30 times 1000 steps"""
    base_statistics = BaseStatistics()
    base_statistics.base_statistics(run_episode=run_episode, episode_runs=1000)
    base_statistics.box_plot()
    print(base_statistics)
