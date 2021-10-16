import iml.const as const
import random

from iml.statistics_base import BaseStatistics

"""This is stateless"""


def next_state(state, action, wall=const.WITHOUT_WALL):
    """ requires state belongs to world const.INITIAL <= state <= const.FINAL
        :return next state when we apply an action"""
    if wall is None:
        wall = []
    if not (const.INITIAL <= state <= const.FINAL):
        raise ValueError('Invalid state')
    move = state
    if action == const.UP:
        next_move = state - const.MOVE_UP_DOWN
        if not (next_move < const.LIMIT_U) and not is_wall(next_move, wall):
            move = next_move
    elif action == const.DOWN:
        next_move = state + const.MOVE_UP_DOWN
        if not (next_move > const.LIMIT_D) and not is_wall(next_move, wall):
            move = next_move
    elif action == const.RIGHT:
        next_move = state + const.MOVE_RIGHT_LEFT
        if state % 10 != const.LIMIT_R and not is_wall(next_move, wall):
            move = next_move
    elif action == const.LEFT:
        next_move = state - const.MOVE_RIGHT_LEFT
        if state % 10 != const.LIMIT_L and not is_wall(next_move, wall):
            move = next_move
    else:
        raise ValueError('Invalid action')
    return move


def is_wall(next_move, wall):
    return next_move in wall


def reward(state, previous_state=None, penalization=False):
    """:return points for that state"""
    if penalization and previous_state is not None and previous_state == state:
        return const.PENALIZATION
    return const.NO_REWARD if not is_final_state(state) else const.REWARD


def is_final_state(state):
    """:return True if the state is equals to goal point defined on const.GOAL"""
    return state == const.GOAL


def random_action():
    """:return random action present on const.ACTIONS (up down left right)"""
    return random.choice(const.ACTIONS)


def end_episode(state, previous_state=None, penalization=False):
    """ :return state, reward, was final state """
    return const.INITIAL if is_final_state(state) else state, reward(state, previous_state, penalization), is_final_state(state)


def run_episode(actions=random_action, execution_times=1000, penalization=False):
    """ execute execution_times the episode
        :return rewards, list of steps done for reach each goal"""
    # initial context
    state = 0
    points = 0
    steps = 0
    numb_steps = []
    # execution_times attempts
    for i in range(execution_times):
        previous_state = state
        # apply random action
        state = next_state(state, actions())
        steps += 1
        # end episode - back to home
        progress = end_episode(state, previous_state, penalization)
        # count many times that reach the reward
        if progress[2]:
            numb_steps.append(steps)
            steps = 0
        state = progress[0]
        points += progress[1]
    return points, numb_steps, []


def run_statistics(actions=random_action, episode_runs=1000, runs_time=30, penalization=False) -> BaseStatistics:
    """ run 30 times 1000 steps
    :return base statistics"""
    base_statistics = BaseStatistics()
    episode: lambda: tuple[int, list[int], list] = lambda: run_episode(actions=actions, execution_times=episode_runs,
                                                                       penalization=penalization)
    base_statistics.base_statistics(run_episode=episode, episode_runs=episode_runs,
                                    runs_time=runs_time)
    return base_statistics
