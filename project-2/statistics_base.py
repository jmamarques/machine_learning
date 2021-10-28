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

    def __str__(self) -> str:
        headers = []
        values = np.array(
            [range(self.run_times + 1)
                , [f'Time for each run in (s):'] + self.time_record
                , [f'Attempts for each run:'] + self.attempts_record
             ])

        if len(self.attempts_record) > 1:
            self.attempts_average = s.mean(self.attempts_record)
        elif len(self.attempts_record) == 1:
            self.attempts_average = self.attempts_record[0]
        if len(self.time_record) > 1:
            self.time_average = s.mean(self.time_record)
        elif len(self.time_record) == 1:
            self.time_average = self.time_record[0]
        table = tabulate(values, headers)
        table_str = "" if self.inactive else f"Sum table: \n" + table.__str__()
        return f"Time average: {self.time_average}\n" \
               + f"Attempts average: {self.attempts_average}\n" \
               + table_str

    def __init__(self, inactive=True) -> None:
        super().__init__()
        self.run_times = 0
        self.time_record = []
        self.attempts_record = []
        self.inactive = inactive

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
