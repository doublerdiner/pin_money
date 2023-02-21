from flask import Flask, Blueprint, render_template, redirect, request
import datetime
from repositories import transaction_repository, account_repository, goal_repository
from models.goal import *
from models.transaction import Transaction
from models.category import Category
from models.vendor import Vendor

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
    # Nearest Goal
    goals = goal_repository.select_all()
    goal = goals[0]
    # Calculations
    available_money = take_home_pay - grand_total
    to_be_saved = goal.savings_target - goal.saved_so_far 
    goal.time_remaining()
    time = goal.goal_comment()   
    return render_template("index.html", title="Home", month=month, year=year, take_home_pay=take_home_pay, pin_money=pin_money, monthly_recurring=monthly_recurring, pin_money_total=pin_money_total, monthly_recurring_total=monthly_recurring_total, goal=goal, grand_total=grand_total, available_money=available_money, to_be_saved=to_be_saved, time=time)

@home_blueprint.route("/home/<id>", methods=['POST'])
def update_goal_home(id):
    goal = goal_repository.select(id)
    name = goal.name
    savings_target = goal.savings_target
    savings_time_frame = goal.savings_time_frame
    saved_so_far = float(goal.saved_so_far) + float(request.form['saved_so_far'])
    goal = Goal(name, savings_target, savings_time_frame, saved_so_far, id)
    goal_repository.update(goal)
    return redirect ("/home")