import pdb
from models.category import Category
from models.goal import Goal
from models.transaction import Transaction
from models.vendor import Vendor

import repositories.category_repository as category_repository
import repositories.goal_repository as goal_repository
import repositories.transaction_repository as transaction_repository
import repositories.vendor_repository as vendor_repository

goal_1 = Goal(2500.00, 1000.00, "2023-06-01")
transaction_1 = Transaction("Cinema", 18.00, "2023-02-17")
vendor_1 = Vendor("ABC Cinema", transaction_1)
category_1 = Category("Entertainment", transaction_1)

pdb.set_trace()