import unittest
from models.category import Category
from models.transaction import Transaction


class TestCategory(unittest.TestCase):
    transaction_1 = Transaction("Cinema", 18.00, "2023-02-17")
    category_1 = Category("Entertainment", transaction_1)

    def test_category_has_name(self):
        self.assertEqual("Entertainment", self.category_1.name)

    def test_category_has_transaction(self):
        self.assertEqual(self.transaction_1, self.category_1.transaction)

    def test_category_has_deactivated_status(self):
        self.assertEqual(False, self.category_1.deactivated)

    def test_category_has_id(self):
        self.assertEqual(None, self.category_1.id)

    def test_category_deactivated_status_change__True(self):
        self.category_1.category_change_deactivated_status()
        self.assertEqual(True, self.category_1.deactivated)
        self.category_1.category_change_deactivated_status()

    def test_category_deactivated_status_change__False(self):
        self.category_1.deactivated = True
        self.category_1.category_change_deactivated_status()
        self.assertEqual(False, self.category_1.deactivated)

    # 17/02/23 - Above tests passed. 