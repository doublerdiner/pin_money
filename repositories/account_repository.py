from db.run_sql import run_sql

from models.account import Account

def save(account):
    sql = "INSERT INTO accounts take_home_pay VALUES %s RETURNING *"
    values = [account.take_home_pay]

def select_all():
    pass

# def select(id):
#     pass

# def delete(id):
#     pass

# def delete_all():
#     pass
# These will not be needed for the app

def update(account):
    pass