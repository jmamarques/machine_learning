import statistics as s
import time
import numpy as np
from tabulate import tabulate
import const
import algorithm

import matplotlib.pyplot as plt


class BaseStatistics:
    run_times: int
    time_record: list
    attempts_record: list

    def __init__(self) -> None:
        super().__init__()
        self.run_times = 0
        self.time_record = []
        self.attempts_record = []

    def __str__(self) -> str:
        return ''

    def base_statistics(self, play, runs_times=30) -> None:
        self.run_times = runs_times
        self.time_record = []
        self.attempts_record = []

        for i in range(runs_times):
            times, attempts = play()
            self.time_record.append(times)
            self.attempts_record.append(attempts)

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
