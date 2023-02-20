import unittest
from models.goal import Goal
from datetime import datetime


class TestGoal(unittest.TestCase):
    goal_1 = Goal("Holiday", 1000.00, "2023-06-01", 500.00)

    def test_goal_has_name(self):
        self.assertEqual("holida", self.goal_1.name)

    def test_goal_has_savings_target(self):
        self.assertEqual(1000.00, self.goal_1.savings_target)

    def test_goal_has_savings_time_frame(self):
        self.assertEqual("2023-06-01", self.goal_1.savings_time_frame)

    def test_goal_has_saved_so_far(self):
        self.assertEqual(500, self.goal_1.saved_so_far)

    def test_goal_has_id(self):
        self.assertEqual(None, self.goal_1.id)

    def test_time_remaining(self):
        answer = self.goal_1.time_remaining()
        self.assertEqual([-19, 4, 0], answer)
        # Will change from day to day

    def test_goal_comment(self):
        self.goal_1.time_remaining()
        answer = self.goal_1.goal_comment()
        self.assertEqual("You have 4 months to meet your goal", answer)
        # Will change from day to day

    def test_goal_calculation(self):
        self.goal_1.time_remaining()
        answer = self.goal_1.goal_calculation()
        self.assertEqual(125.00, answer)
        # Will change from day to day

# 17/02/23 - Above tests passed.

