import statistics as s
import time
import numpy as np
from tabulate import tabulate
import const
import algorithm

import matplotlib.pyplot as plt


class BaseStatistics:
    inactive: bool
    run_times: int
    time_record: list
    time_average: float = 0
    attempts_record: list
    attempts_average: float = 0
    master_minds: list
    goal_reach: int = 0

    def __str__(self) -> str:
        return f"Time average: {self.time_average}\n" \
               + f"Attempts average: {self.attempts_average}\n" \
               + f"Reach goal: {self.goal_reach}/{self.run_times}\n"

    def __init__(self, inactive=True) -> None:
        super().__init__()
        self.run_times = 0
        self.time_record = []
        self.attempts_record = []
        self.inactive = inactive
        self.master_minds = []

    def base_statistics(self, play, runs_times=30) -> None:
        self.run_times = runs_times
        self.time_record = []
        self.attempts_record = []

        for i in range(runs_times):
            times, attempts, mm_mind = play()
            self.time_record.append(times)
            self.attempts_record.append(attempts)
            self.master_minds.append(mm_mind)

        if len(self.attempts_record) > 1:
            self.attempts_average = s.mean(self.attempts_record)
        elif len(self.attempts_record) == 1:
            self.attempts_average = self.attempts_record[0]
        if len(self.time_record) > 1:
            self.time_average = s.mean(self.time_record)
        elif len(self.time_record) == 1:
            self.time_average = self.time_record[0]
        for mm_mind in self.master_minds:
            if mm_mind.final_guess == mm_mind.final_goal:
                self.goal_reach += 1


    def box_plot(self):
        self.box_plot_dev(self.time_record, "Execution Time")
        self.box_plot_dev(self.attempts_record, "Attempts")

    @staticmethod
    def box_plot_dev(values, title):
        # Creating plot
        plt.boxplot(values)
        plt.title(title)
        plt.show()

    @staticmethod
    def linear_plot_dev(val_x, val_y, title_x, title_y, title):
        plt.plot(val_x, val_y)
        plt.title(title)
        plt.xlabel(title_x)
        plt.ylabel(title_y)
        plt.show()
