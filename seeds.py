import pdb
from models.category import Category
from models.goal import Goal
from models.transaction import Transaction
from models.vendor import Vendor
from models.account import Account

import repositories.category_repository as category_repository
import repositories.goal_repository as goal_repository
import repositories.transaction_repository as transaction_repository
import repositories.vendor_repository as vendor_repository
import repositories.account_repository as account_repository


# transaction_repository.delete_all()
account_repository.delete_all()
goal_repository.delete_all()
category_repository.delete_all()

goal_1 = Goal(1000.00, "2023-06-01", 500.00)
goal_repository.save(goal_1)

vendor_1 = Vendor("ABC Cinema")
category_1 = Category("Entertainment")
category_repository.save(category_1)


account_1 = Account(2500.00)
account_repository.save(account_1)
transaction_1 = Transaction("Cinema", 18.00, "2023-02-17", category_1, vendor_1)
# transaction_repository.save(transaction_1)

pdb.set_trace()