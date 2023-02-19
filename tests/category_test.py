import unittest
from models.category import Category


class TestCategory(unittest.TestCase):
    category_1 = Category("Entertainment")

    def test_category_has_name(self):
        self.assertEqual("Entertainment", self.category_1.name)

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