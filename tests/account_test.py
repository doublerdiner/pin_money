import unittest
from models.account import Account


class TestAccount(unittest.TestCase):
    account_1 = Account(2500.00)

    def test_account_has_take_home_pay(self):
        self.assertEqual(2500, self.account_1.take_home_pay)

    def test_account_has_id(self):
        self.assertEqual(None, self.account_1.id)