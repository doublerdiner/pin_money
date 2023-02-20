from db.run_sql import run_sql

from models.transaction import Transaction
from models.category import Category
from models.vendor import Vendor
import repositories.category_repository as category_repository
import repositories.vendor_repository as vendor_repository

# This repository was tested on 19/02/23.
# All passed

def save(transaction):
    sql = "INSERT INTO transactions (name, cost, date, category_id, vendor_id, monthly_recurring, notes) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.name, transaction.cost, transaction.date, transaction.category.id, transaction.vendor.id, transaction.monthly_recurring, transaction.notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY date ASC"
    results = run_sql(sql)
    for row in results:
        category = category_repository.select(row['category_id'])
        vendor = vendor_repository.select(row['vendor_id'])
        transaction = Transaction(row['name'], row['cost'], row['date'], category, vendor, row['monthly_recurring'], row['notes'], row['id'])
        transactions.append(transaction)
    return transactions

def select_all_name():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY name ASC"
    results = run_sql(sql)
    for row in results:
        category = category_repository.select(row['category_id'])
        vendor = vendor_repository.select(row['vendor_id'])
        transaction = Transaction(row['name'], row['cost'], row['date'], category, vendor, row['monthly_recurring'], row['notes'], row['id'])
        transactions.append(transaction)
    return transactions

def select_all_cost():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY CAST(cost AS DECIMAL(10,2)) ASC"
    results = run_sql(sql)
    for row in results:
        category = category_repository.select(row['category_id'])
        vendor = vendor_repository.select(row['vendor_id'])
        transaction = Transaction(row['name'], row['cost'], row['date'], category, vendor, row['monthly_recurring'], row['notes'], row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        category = category_repository.select(result['category_id'])
        vendor = vendor_repository.select(result['vendor_id'])
        transaction = Transaction(result['name'], result['cost'], result['date'], category, vendor, result['monthly_recurring'], result['notes'], result['id'])
    return transaction

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def update(transaction):
    sql = "UPDATE transactions SET (name, cost, date, category_id, vendor_id, monthly_recurring, notes) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [transaction.name, transaction.cost, transaction.date, transaction.category.id, transaction.vendor.id, transaction.monthly_recurring, transaction.notes, transaction.id]
    run_sql(sql, values)

    # tested to this point

    # TESTING REQUIRED ...

def transactions_for_this_month(month_int):
    transactions = []
    select = select_all()
    for transaction in select:
        if transaction.obtain_month_int() == int(month_int):
            transactions.append(transaction)
    return transactions

def pin_money_transactions_for_this_month(month_int):
    transactions = []
    total_transactions = transactions_for_this_month(month_int)
    for transaction in total_transactions:
        if not transaction.monthly_recurring:
            transactions.append(transaction)
    return transactions

def monthly_recurring_transactions():
    transactions = []
    total_transactions = select_all()
    for transaction in total_transactions:
        if transaction.monthly_recurring:
            transactions.append(transaction)
    return transactions

def total_transactions(list):
    total=0
    for transaction in list:
        total += transaction.cost
    return total



