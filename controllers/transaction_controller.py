from flask import Flask, Blueprint, render_template, redirect
import datetime
from repositories import transaction_repository, account_repository

transaction_blueprint = Blueprint("transaction", __name__)

# INDEX
# GET TRANSACTIONS
@transaction_blueprint.route('/transactions')
def transactions():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    month_int = today.month
    year = today.strftime("%Y")
    # transactions
    transactions = transaction_repository.transactions_for_this_month(month_int)
    pin_money = transaction_repository.pin_money_transactions_for_this_month(month_int)
    monthly_recurring = transaction_repository.monthly_recurring_transactions(month_int)
    transactions_total = transaction_repository.total_transactions(transactions)
    pin_money_total = transaction_repository.total_transactions(pin_money)
    monthly_recurring_total = transaction_repository.total_transactions(monthly_recurring)
    # take_home_pay
    accounts = account_repository.select_all()
    account = accounts[0]
    take_home_pay = account.take_home_pay
    
    return render_template("transactions/index.html", title="Transactions", month=month, year=year, take_home_pay=take_home_pay, pin_money=pin_money, monthly_recurring=monthly_recurring, transactions_total=transactions_total, pin_money_total=pin_money_total, monthly_recurring_total=monthly_recurring_total)
