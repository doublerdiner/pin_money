import unittest
from models.goal import Goal
from datetime import datetime


class TestGoal(unittest.TestCase):
    goal_1 = Goal(2500.00, 1000.00, "2023-06-01")

    def test_goal_has_monthly_take_home_pay(self):
        self.assertEqual(2500.00, self.goal_1.monthly_take_home_pay)

    def test_goal_has_savings_target(self):
        self.assertEqual(1000.00, self.goal_1.savings_target)

    def test_goal_has_savings_time_frame(self):
        self.assertEqual(datetime.strptime("2023-06-01", "%Y-%m-%d"), self.goal_1.savings_time_frame)

    def test_goal_has_id(self):
        self.assertEqual(None, self.goal_1.id)

    def test_time_remaining(self):
        answer = self.goal_1.time_remaining()
        self.assertEqual([-16, 4, 0], answer)
        # Will change from day to day

    def test_goal_comment(self):
        self.goal_1.time_remaining()
        answer = self.goal_1.goal_comment()
        self.assertEqual("You have 4 months to meet your goal", answer)
        # Will change from day to day

    def test_goal_calculation(self):
        self.goal_1.time_remaining()
        answer = self.goal_1.goal_calculation()
        self.assertEqual(250.00, answer)
        # Will change from day to day

# 17/02/23 - Above tests passed.

