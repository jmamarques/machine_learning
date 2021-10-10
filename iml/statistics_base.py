import statistics as s
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

    def __init__(self) -> None:
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

    def __str__(self) -> str:
        return f"Rewards for the {self.run_times} tests: {self.total_reward}\n" \
               + f"Average reward per step in these {self.episode_runs} steps: {self.average_reward}\n" \
               + f"Run time for the {self.run_times} tests: {self.num_runs}\n" \
               + f"Average of number of steps to reach-goal: {self.average}\n" \
               + f"Standard-deviation of number of steps to reach-goal: {self.standard_deviation}\n"

    def base_statistics(self, run_episode, runs_time=30, episode_runs=1000) -> ([], [], []):
        """ :return :0 points
                    :1 steps
                    :2 runs
        """
        self.__init__()
        self.run_times = runs_time
        self.episode_runs = episode_runs
        for i in range(runs_time):
            run_points, run_numb_steps = run_episode()
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
        return self.points, self.steps, self.runs

    def box_plot(self):
        self.__box_plot_dev(self.points, "Reward")
        self.__box_plot_dev(self.runs, "Run-time")
        self.__box_plot_dev(self.steps, "Steps")

    @staticmethod
    def __box_plot_dev(values, title):
        # Creating plot
        plt.boxplot(values)
        plt.title(title)
        plt.show()
