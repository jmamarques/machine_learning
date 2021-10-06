import unittest
import random
import iml.environment as env
import iml.const as const


class TestEnvironment(unittest.TestCase):
    def test_next_state(self):
        self.assertRaises(ValueError, lambda: env.next_state(const.INITIAL, "INVALID action"))
        self.assertRaises(ValueError, lambda: env.next_state(const.INITIAL-1, const.UP))
        # test initial position
        self.assertEqual(env.next_state(const.INITIAL, const.UP), const.INITIAL)
        self.assertEqual(env.next_state(const.INITIAL, const.LEFT), const.INITIAL)
        self.assertEqual(env.next_state(const.INITIAL, const.DOWN), const.INITIAL + const.MOVE_UP_DOWN)
        self.assertEqual(env.next_state(const.INITIAL, const.RIGHT), const.INITIAL + const.MOVE_RIGHT_LEFT)
        # middle
        state = 55
        self.assertEqual(env.next_state(state, const.UP), state - const.MOVE_UP_DOWN)
        self.assertEqual(env.next_state(state, const.LEFT), state - const.MOVE_RIGHT_LEFT)
        self.assertEqual(env.next_state(state, const.DOWN), state + const.MOVE_UP_DOWN)
        self.assertEqual(env.next_state(state, const.RIGHT), state + const.MOVE_RIGHT_LEFT)
