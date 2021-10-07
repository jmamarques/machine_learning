import iml.const as const
import random
import statistics as s
import matplotlib.pyplot as plt

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


def run_episode_1000x(actions=random_action()):
    """ execute 1000x the episode
        :return rewards, list of steps done for reach each goal"""
    # initial context
    state = 0
    points = 0
    steps = 0
    numb_steps = []
    # 1000 attempts
    for i in range(1000):
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
    # initialization
    total_reward = 0
    average_reward = 0
    steps = []
    points = []
    runs = []
    # repeat 30 times
    for i in range(30):
        res = run_episode_1000x()
        points.append(res[0])
        total_reward += res[0]
        # put the steps in auxiliary array
        for step in res[1]:
            steps.append(step)
        runs.append(len(res[1]))
    # avoid arithmetic exception
    if total_reward != 0:
        average_reward = total_reward / (30 * 1000)
    average = s.mean(steps)
    num_runs = len(steps)
    standard_deviation = s.stdev(steps)

    print("Rewards for the 30 tests: %d" % total_reward)
    print("Average reward per step in these 1000 steps: %f" % average_reward)
    print("Run time for the 30 tests: %d" % num_runs)
    print("Average of number of steps to reach-goal: %f" % average)
    print("Standard-deviation of number of steps to reach-goal: %f" % standard_deviation)

    # Creating plot Reward
    plt.boxplot(points)
    plt.title("Reward")
    plt.show()
    # Creating plot Run-time
    plt.boxplot(runs)
    plt.title("Run-time")
    plt.show()
    # Creating plot Steps
    plt.boxplot(steps)
    plt.title("Steps")
    plt.show()


# run_statistics()
