from db.run_sql import run_sql

from models.category import Category
from models.transaction import Transaction
from repositories import vendor_repository

# This repository was tested on 19/02/23.
# All passed.

def save(category):
    sql = "INSERT INTO categories (name, active) VALUES (%s, %s) RETURNING *"
    values = [category.name, category.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id
    return category

def select_all():
    categories = []
    sql = "SELECT * FROM categories ORDER BY name ASC"
    results = run_sql(sql)
    for row in results:
        category = Category(row['name'], row['active'], row['id'])
        categories.append(category)
    return categories

def select(id):
    category = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        category = Category(result['name'], result['active'], result['id'])
    return category

def delete(id):
    sql = "DELETE FROM categories WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)

def update(category):
    sql = "UPDATE categories SET (name, active) = (%s, %s) WHERE id = %s"
    values = [category.name, category.active, category.id]
    run_sql(sql, values)


def category_transactions(category):
    transactions = []
    sql = "SELECT * FROM transactions WHERE category_id = %s ORDER by date ASC"
    values = [category.id]
    results = run_sql(sql, values)
    for row in results:
        category = select(row['category_id'])
        vendor = vendor_repository.select(row['vendor_id'])
        transaction = Transaction(row['name'], row['cost'], row['date'], category, vendor, row['monthly_recurring'], row['notes'], row['id'])
        transactions.append(transaction)
    return transactions
