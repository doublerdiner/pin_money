from db.run_sql import run_sql

from models.vendor import Vendor
from models.transaction import Transaction

# This repository was tested on 19/02/23.
# All passed.

def save(vendor):
    sql = "INSERT INTO vendors (name, active) VALUES (%s, %s) RETURNING *"
    values = [vendor.name, vendor.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    vendor.id = id
    return vendor

def select_all():
    vendors = []
    sql = "SELECT * FROM vendors ORDER BY name ASC"
    results = run_sql(sql)
    for row in results:
        vendor = Vendor(row['name'], row['active'], row['id'])
        vendors.append(vendor)
    return vendors

def select(id):
    vendor = None
    sql = "SELECT * FROM vendors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        vendor = Vendor(result['name'], result['active'], result['id'])
    return vendor

def delete(id):
    sql = "DELETE FROM vendors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM vendors"
    run_sql(sql)

def update(vendor):
    sql = "UPDATE vendors SET (name, active) = (%s, %s) WHERE id = %s"
    values = [vendor.name, vendor.active, vendor.id]
    run_sql(sql, values)


def vendor_transactions(vendor):
    transactions = []
    sql = "SELECT * FROM transactions WHERE vendor_id = %s"
    values = [vendor.id]
    results = run_sql(sql, values)
    for row in results:
        transaction = Transaction(row['name'], row['cost'], row['date'], row['category_id'], row['vendor_id'], row['monthly_recurring'], row['notes'], row['id'])
        transactions.append(transaction)
    return transactions
