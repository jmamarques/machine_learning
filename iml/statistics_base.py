import statistics as s
import time
import numpy as np
from tabulate import tabulate

import matplotlib.pyplot as plt


class BaseStatistics:
    total_reward: float
    average_reward: float
    steps: list
    points: list
    runs: list
    average_reward: float
    average: float
    num_runs: int
    standard_deviation: float
    run_times: int
    episode_runs: int
    time_executions: list
    extra_stats: list

    def __init__(self) -> None:
        """

        :rtype: object
        """
        super().__init__()
        self.total_reward = 0
        self.average_reward = 0
        self.steps = []
        self.points = []
        self.runs = []
        self.average_reward = 0.0
        self.average = 0.0
        self.num_runs = 0
        self.standard_deviation = 0.0
        self.run_times = 30
        self.episode_runs = 1000
        self.time_executions = []
        self.extra_stats = []

    def __str__(self) -> str:
        headers = []
        values = np.array(
            [range(len(self.time_executions) + 1)
                , [f'Time for each {self.episode_runs} run in (s):'] + self.time_executions
                , [f'Rewards for each {self.episode_runs} run:'] + self.points
                , [f'Goals reached for each {self.episode_runs} run:'] + self.runs
                , [f'Steps Average for each run:'] + self.get_steps_average_by_run()
             # , ['Stats:'] + self.extra_stats
             ])
        table = tabulate(values, headers)

        return f"Rewards for the {self.run_times} tests: {self.total_reward}\n" \
               + f"Average reward per step in these {self.episode_runs} steps: {self.average_reward}\n" \
               + f"Run time for the {self.run_times} tests: {self.num_runs}\n" \
               + f"Average of number of steps to reach-goal: {self.average}\n" \
               + f"Standard-deviation of number of steps to reach-goal: {self.standard_deviation}\n" \
               + f"Sum table: \n" \
               + table.__str__()

    def base_statistics(self, run_episode, runs_time=30, episode_runs=1000) -> ([], [], []):
        """ :return :0 points
                    :1 steps
                    :2 runs
                    :4 execution time
                    :5 extra fields for each run episode
        """
        self.__init__()
        self.run_times = runs_time
        self.episode_runs = episode_runs
        for i in range(runs_time):
            start_time = time.time()
            run_points, run_numb_steps, extra = run_episode()
            self.time_executions.append(time.time() - start_time)
            self.extra_stats.append(extra)
            self.points.append(run_points)
            self.total_reward += run_points
            # put the steps in auxiliary array
            for step in run_numb_steps:
                self.steps.append(step)
            self.runs.append(len(run_numb_steps))
            # avoid arithmetic exception
        if self.total_reward != 0:
            self.average_reward = self.total_reward / (runs_time * episode_runs)
        self.average = s.mean(self.steps)
        self.num_runs = len(self.steps)
        self.standard_deviation = s.stdev(self.steps)
        return self.points, self.steps, self.runs, self.time_executions, self.extra_stats

    def box_plot(self):
        self.__box_plot_dev(self.points, "Reward")
        self.__box_plot_dev(self.runs, "Run-time")
        self.__box_plot_dev(self.steps, "Steps")

    def linear_plot_steps_reward(self):
        steps_average_by_run = self.get_steps_average_by_run()
        self.__linear_plot_dev(steps_average_by_run, self.points, 'steps', 'reward',
                               'The steps (x-axis) vs avg reward (y-axis)')

    def get_steps_average_by_run(self) -> list:
        steps_average_by_run = []
        index = 0
        for run in self.runs:
            average: float = 0.0
            if run != 0:
                for i in range(index, run + index):
                    average += self.steps[i]
                average /= run
                index += run
            steps_average_by_run.append(average)
        return steps_average_by_run

    @staticmethod
    def __box_plot_dev(values, title):
        # Creating plot
        plt.boxplot(values)
        plt.title(title)
        plt.show()

    @staticmethod
    def __linear_plot_dev(val_x, val_y, title_x, title_y, title):
        plt.plot(val_x, val_y)
        plt.title(title)
        plt.xlabel(title_x)
        plt.ylabel(title_y)
        plt.show()
