import const
import random


def nextState(state, action):
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
    return const.NO_REWARD if not is_final_state(state) else const.REWARD


def is_final_state(state):
    return state == const.GOAL


def random_action():
    return random.choice(const.ACTIONS)


def run_episode_1000x():
    # initial context
    state = 0
    points = 0
    count = 0
    for i in range(1000):
        # apply random action
        state = nextState(state, random_action())
        # end episode - back to home
        progress = end_episode(state)
        # count many times that reach the reward
        if progress[0] != state:
            count += 1
        state = progress[0]
        points += progress[1]
    return points, count


def end_episode(state):
    return const.INITIAL if is_final_state(state) else state, reward(state)


print(run_episode_1000x())
