class Statistics:
    total_reward: float
    average_reward: float
    steps: list
    points: list
    runs: list

    def __init__(self) -> None:
        super().__init__()
        self.total_reward = 0
        self.average_reward = 0
        self.steps = []
        self.points = []
        self.runs = []


