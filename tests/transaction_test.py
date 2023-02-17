import unittest
from models.transaction import Transaction
from datetime import datetime


class TestTransaction(unittest.TestCase):
    transaction_1 = Transaction("Cinema", 18.00, "2023-02-17")

    def test_transaction_has_name(self):
        self.assertEqual("Cinema", self.transaction_1.name)

    def test_transaction_has_cost(self):
        self.assertEqual(18.00, self.transaction_1.cost)

    def test_transaction_has_date(self):
        self.assertEqual(datetime.strptime("2023-02-17", "%Y-%m-%d"), self.transaction_1.date)

    def test_transaction_has_monthly_recurring(self):
        self.assertEqual(False, self.transaction_1.monthly_recurring)

    def test_transaction_has_notes(self):
        self.assertEqual(None, self.transaction_1.notes)

    def test_transaction_has_id(self):
        self.assertEqual(None, self.transaction_1.id)

    def test_transaction_monthly_recurring_status_change__True(self):
        self.transaction_1.change_monthly_recurring()
        self.assertEqual(True, self.transaction_1.monthly_recurring)
        self.transaction_1.change_monthly_recurring()

    def test_transaction_monthly_recurring_status_change__False(self):
        self.transaction_1.monthly_recurring = True
        self.transaction_1.change_monthly_recurring()
        self.assertEqual(False, self.transaction_1.monthly_recurring)

# 17/02/23 - Above tests passed