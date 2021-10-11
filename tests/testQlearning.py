import unittest

import iml.const as const
import iml.q_learning as q
import iml.environment as env


class TestEnvironment(unittest.TestCase):
    def test_algorithm_q_learning(self):
        pass

    def test_run_statistics(self):
        run = q.QLearning()
        self.assertIsNotNone(run.run_statistics(), "Run statistics without problem")
