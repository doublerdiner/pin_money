from db.run_sql import run_sql

from models.account import Account

# This repository was tested on 19/02/23.
# All passed.

def save(account):
    sql = "INSERT INTO accounts (take_home_pay) VALUES (%s) RETURNING *"
    values = [account.take_home_pay]
    results = run_sql(sql, values)
    id = results[0]['id']
    account.id = id
    return account

def select_all():
    accounts = []
    sql = "SELECT * FROM accounts"
    results = run_sql(sql)
    for row in results:
        account = Account(row['take_home_pay'], row['id'])
        accounts.append(account)
    return accounts

def select(id):
    account = None
    sql = "SELECT * FROM accounts WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        account = Account(result['take_home_pay'], result['id'])
    return account

def delete(id):
    sql = "DELETE FROM accounts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM accounts"
    run_sql(sql)


def update(account):
    sql = "UPDATE accounts SET take_home_pay = %s WHERE id = %s"
    values = [account.take_home_pay, account.id]
    run_sql(sql, values)