import unittest
from models.transaction import Transaction
from models.category import Category
from models.vendor import Vendor


class TestTransaction(unittest.TestCase):
    category_1 = Category("Entertainment")
    vendor_1 = Vendor("ABC Cinema")
    transaction_1 = Transaction("Cinema", 18.00, "2023-02-17", category_1, vendor_1)

    def test_transaction_has_name(self):
        self.assertEqual("Cinema", self.transaction_1.name)

    def test_transaction_has_cost(self):
        self.assertEqual(18.00, self.transaction_1.cost)

    def test_transaction_has_date(self):
        self.assertEqual("2023-02-17", self.transaction_1.date)

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

    def test_transaction_has_category(self):
        self.assertEqual(self.category_1, self.transaction_1.category)

    def test_transaction_has_vendor(self):
        self.assertEqual(self.vendor_1, self.transaction_1.vendor)

# 19/02/23 Above tests passed.

    def test_obtain_month_int(self):
        answer = self.transaction_1.obtain_month_int()
        self.assertEqual(2, answer)

# 20/02/23 Above tests passed. 