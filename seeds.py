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


transaction_repository.delete_all()
account_repository.delete_all()
goal_repository.delete_all()
category_repository.delete_all()
vendor_repository.delete_all()

goal_1 = Goal("Holiday", 1000.00, "2023-06-01", 500.00)
goal_2 = Goal("TV", 300.00, "2023-08-15", 0.00)
goal_repository.save(goal_1)
goal_repository.save(goal_2)
vendor_1 = Vendor("ABC Cinema")
vendor_2 = Vendor("Pepperoni Perfection")
vendor_3 = Vendor("The Train Co.")
vendor_4 = Vendor("High Dive Bar")
vendor_5 = Vendor("Rent")
vendor_repository.save(vendor_1)
vendor_repository.save(vendor_2)
vendor_repository.save(vendor_3)
vendor_repository.save(vendor_4)
vendor_repository.save(vendor_5)
category_1 = Category("Entertainment")
category_2 = Category("Food & Drinks")
category_3 = Category("Transport")
category_4 = Category("Rent")
category_repository.save(category_1)
category_repository.save(category_2)
category_repository.save(category_3)
category_repository.save(category_4)
account_1 = Account(2500.00)
account_repository.save(account_1)
transaction_1 = Transaction("Cinema", 18.00, "2023-02-17", category_1, vendor_1)
transaction_2 = Transaction("Dinner", 60.00, "2023-02-19", category_2, vendor_2)
transaction_3 = Transaction("Train Journey into Town", 4.80, "2023-02-23", category_3, vendor_3)
transaction_4 = Transaction("Gig at the High Dive Bar", 22.20, "2023-02-25", category_1, vendor_4)
transaction_5 = Transaction("Drinks After Work", 33.10, "2023-03-02", category_2, vendor_4)
transaction_6 = Transaction("Rent", 450.00, "2023-02-01", category_4, vendor_5, True)
transaction_repository.save(transaction_1)
transaction_repository.save(transaction_2)
transaction_repository.save(transaction_3)
transaction_repository.save(transaction_4)
transaction_repository.save(transaction_5)
transaction_repository.save(transaction_6)

pdb.set_trace()