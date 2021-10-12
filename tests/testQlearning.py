import unittest

import iml.const as const
import iml.q_learning as q
import iml.environment as env


class TestEnvironment(unittest.TestCase):
    def test_algorithm_q_learning(self):
        pass

    def test_run_statistics(self):
        run = q.QLearning()
        self.assertIsNotNone(run.run_statistics(episode_runs=1000), "Run statistics without problem")
        var = run.run_statistics(actions=run.best_action, runs_time=1)
        var.box_plot()
        self.assertIsNotNone(var, "Run statistics without problem")
        self.assertIsNotNone(var.__str__(), "to string of statistics")
