from flask import Flask, Blueprint, render_template, redirect, request
from repositories import category_repository
from models.category import Category

category_blueprint = Blueprint("category", __name__)

# NEW
@category_blueprint.route('/categories/new')
def new_category():
    return render_template('categories/new.html', title="New Category") 

# CREATE
@category_blueprint.route('/categories', methods=['POST'])
def create_category():
    name = request.form['name']
    category = Category(name)
    category_repository.save(category)
    return redirect ("/settings")

# SHOW / EDIT
@category_blueprint.route("/categories/<id>")
def show_category(id):
    category = category_repository.select(id)
    transactions = category_repository.category_transactions(category)
    total=0
    for transaction in transactions:
        total += transaction.cost
    return render_template("categories/show.html", title="View Category", transactions=transactions, category=category, total=total)

# # EDIT
# @category_blueprint.route('/categories/edit/<id>')
# def edit_category(id):
#     category = category_repository.select(id)
#     return render_template("categories/edit.html", title="Edit Category", category=category)

# UPDATE
@category_blueprint.route("/categories/<id>", methods=['POST'])
def update_category(id):
    name = request.form['name']
    if request.form['activate'] == "deactivate":
        active = False
    else:
        active = True
    category = Category(name, active, id)
    category_repository.update(category)
    return redirect ("/settings")