import unittest
from models.vendor import Vendor
from models.transaction import Transaction


class TestVendor(unittest.TestCase):
    transaction_1 = Transaction("Cinema", 18.00, "17/02/2023")
    vendor_1 = Vendor("ABC Cinema", transaction_1)

    def test_vendor_has_name(self):
        self.assertEqual("ABC Cinema", self.vendor_1.name)

    def test_vendor_has_transaction(self):
        self.assertEqual(self.transaction_1, self.vendor_1.transaction)

    def test_vendor_has_deactivated_status(self):
        self.assertEqual(False, self.vendor_1.deactivated)

    def test_vendor_has_id(self):
        self.assertEqual(None, self.vendor_1.id)

    def test_vendor_deactivated_status_change__True(self):
        self.vendor_1.vendor_change_deactivated_status()
        self.assertEqual(True, self.vendor_1.deactivated)
        self.vendor_1.vendor_change_deactivated_status()

    def test_vendor_deactivated_status_change__False(self):
        self.vendor_1.deactivated = True
        self.vendor_1.vendor_change_deactivated_status()
        self.assertEqual(False, self.vendor_1.deactivated)

# 17/02/23 - Above tests passed