from flask import Flask, Blueprint, render_template, redirect, request
import datetime
from repositories import account_repository, category_repository, vendor_repository
from models.account import Account
from models.category import Category
from models.vendor import Vendor

settings_blueprint = Blueprint("settings", __name__)

# INDEX
# GET '/account'
@settings_blueprint.route('/settings')
def settings():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    # transactions
    accounts = account_repository.select_all()
    account = accounts[0]
    categories = category_repository.select_all()
    vendors = vendor_repository.select_all()
    return render_template("settings/index.html", title="Settings", month=month, year=year, account=account, categories=categories, vendors=vendors)

@settings_blueprint.route("/settings", methods=['POST'])
def update_settings():
    accounts = account_repository.select_all()
    account = accounts[0]
    take_home_pay = request.form['take_home_pay']
    account = Account(take_home_pay, account.id)
    account_repository.update(account)
    return redirect ("/settings")
