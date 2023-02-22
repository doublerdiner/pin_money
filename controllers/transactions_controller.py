from flask import Flask, Blueprint, render_template, request, redirect
import datetime
from repositories import transaction_repository, category_repository, vendor_repository
from models.transaction import Transaction

transactions_blueprint = Blueprint("transactions", __name__)

# INDEX
# GET TRANSACTIONS
@transactions_blueprint.route('/transactions')
def transactions():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    # transactions
    transactions = transaction_repository.select_all()
    total=0
    for transaction in transactions:
        total += transaction.cost
    return render_template("transactions/index.html", title="All Transactions", month=month, year=year, transactions = transactions, total=total)

@transactions_blueprint.route('/transactions/cost')
def transactions_cost():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    # transactions
    transactions = transaction_repository.select_all_cost()
    total=0
    for transaction in transactions:
        total += transaction.cost
    return render_template("transactions/index_cost.html", title="All Transactions", month=month, year=year, transactions = transactions, total=total)

@transactions_blueprint.route('/transactions/name')
def transactions_name():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    # transactions
    transactions = transaction_repository.select_all_name()
    total=0
    for transaction in transactions:
        total += transaction.cost
    return render_template("transactions/index_name.html", title="All Transactions", month=month, year=year, transactions = transactions, total=total)

# NEW
# GET '/transactions/new'
@transactions_blueprint.route('/transactions/new')
def new_transaction():
    today = datetime.datetime.now()
    categories = category_repository.select_all()
    vendors = vendor_repository.select_all()
    for category in categories:
        if not category.active:
            categories.remove(category)
    for vendor in vendors:
        if not vendor.active:
            vendors.remove(vendor)    
    return render_template('transactions/new.html', title="New Transaction", categories=categories, vendors=vendors, today=today)

# CREATE
# POST '/transactions'
@transactions_blueprint.route('/transactions', methods=['POST'])
def create_transaction():
    name = request.form['name']
    cost = request.form['cost']
    date = request.form['date']
    category = category_repository.select(request.form['category_id'])
    vendor = vendor_repository.select(request.form['vendor_id'])
    if request.form['monthly_recurring'] == "true":
        monthly_recurring = True
    else:
        monthly_recurring = False
    notes = request.form['notes']
    transaction = Transaction(name, cost, date, category, vendor, monthly_recurring, notes)
    transaction_repository.save(transaction)
    return redirect ("/transactions")

# SHOW
# GET '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>")
def show_transaction(id):
    transaction = transaction_repository.select(id)
    categories = category_repository.select_all()
    vendors = vendor_repository.select_all()
    for category in categories:
        if category.name == transaction.category.name:
            categories.remove(category)
    for vendor in vendors:
        if vendor.name == transaction.vendor.name:
            vendors.remove(vendor)  
    return render_template("transactions/show.html", title="View Transaction", transaction=transaction, categories=categories, vendors=vendors)

# UPDATE
# PUT '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    name = request.form['name']
    cost = request.form['cost']
    date = request.form['date']
    category = category_repository.select(request.form['category_id'])
    vendor = vendor_repository.select(request.form['vendor_id'])
    if request.form['monthly_recurring'] == "true":
        monthly_recurring = True
    else:
        monthly_recurring = False
    notes = request.form['notes']
    transaction = Transaction(name, cost, date, category, vendor, monthly_recurring, notes, id)
    transaction_repository.update(transaction)
    return redirect ("/transactions")

# DELETE
# DELETE '/transactions/<id>'
@transactions_blueprint.route("/transactions/delete/<id>", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")
