from flask import Flask, Blueprint, render_template, request, redirect
import datetime
from repositories import transaction_repository, category_repository, vendor_repository
from models.transaction import Transaction

transaction_blueprint = Blueprint("transaction", __name__)

# INDEX
# GET TRANSACTIONS
@transaction_blueprint.route('/transactions')
def transactions():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    # transactions
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", title="All Transactions", month=month, year=year, transactions = transactions)

@transaction_blueprint.route('/transactions/cost')
def transactions_cost():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    # transactions
    transactions = transaction_repository.select_all_cost()
    return render_template("transactions/index_cost.html", title="All Transactions", month=month, year=year, transactions = transactions)

@transaction_blueprint.route('/transactions/date')
def transactions_name():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    # transactions
    transactions = transaction_repository.select_all_name()
    return render_template("transactions/index_name.html", title="All Transactions", month=month, year=year, transactions = transactions)

# NEW
# GET '/transactions/new'
@transaction_blueprint.route('/transactions/new')
def new_transaction():
    today = datetime.datetime.now()
    categories = category_repository.select_all()
    vendors = vendor_repository.select_all()
    return render_template('transactions/new.html', title="New Transaction", categories=categories, vendors=vendors, today=today)

# CREATE
# POST '/transactions'
@transaction_blueprint.route('/transactions', methods=['POST'])
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
@transaction_blueprint.route("/transactions/<id>")
def show_transaction(id):
    transaction = transaction_repository.select(id)
    categories = category_repository.select_all()
    vendors = vendor_repository.select_all()
    return render_template("transactions/show.html", title="View Transaction", transaction=transaction, categories=categories, vendors=vendors)

# EDIT
# GET 'transactions/<id>/edit'
@transaction_blueprint.route('/transactions/edit/<id>')
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    categories = category_repository.select_all()
    vendors = vendor_repository.select_all()
    return render_template("transactions/edit.html", title="Edit Transaction", transaction=transaction, categories=categories, vendors=vendors)

# UPDATE
# PUT '/transactions/<id>'
@transaction_blueprint.route("/transactions/<id>", methods=['POST'])
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
@transaction_blueprint.route("/transactions/delete/<id>", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")
