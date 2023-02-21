from flask import Flask, Blueprint, render_template, redirect
import datetime
from repositories import transaction_repository, account_repository, goal_repository

home_blueprint = Blueprint("home", __name__)

# INDEX
# DISPLAY HOME
@home_blueprint.route('/home')
def home():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    month_int = today.month
    year = today.strftime("%Y")
    # transactions
    pin_money = transaction_repository.pin_money_transactions_for_this_month(month_int)
    monthly_recurring = transaction_repository.monthly_recurring_transactions()
    pin_money_total = transaction_repository.total_transactions(pin_money)
    monthly_recurring_total = transaction_repository.total_transactions(monthly_recurring)
    grand_total = pin_money_total+monthly_recurring_total
    # take_home_pay
    accounts = account_repository.select_all()
    account = accounts[0]
    take_home_pay = account.take_home_pay
    # Calculations
    available_money = take_home_pay - grand_total

    # Nearest Goal
    goals = goal_repository.select_all()
    goal = goals[0]
       
    return render_template("index.html", title="Home", month=month, year=year, take_home_pay=take_home_pay, pin_money=pin_money, monthly_recurring=monthly_recurring, pin_money_total=pin_money_total, monthly_recurring_total=monthly_recurring_total, goal=goal, grand_total=grand_total, available_money=available_money)

