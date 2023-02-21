from flask import Flask, Blueprint, render_template, redirect, request
from repositories import vendor_repository
from models.vendor import Vendor
from models.transaction import Transaction

vendor_blueprint = Blueprint("vendor", __name__)

# NEW
@vendor_blueprint.route('/vendors/new')
def new_vendor():
    return render_template('vendors/new.html', title="New Vendor") 

# CREATE
@vendor_blueprint.route('/vendors', methods=['POST'])
def create_vendor():
    name = request.form['name']
    vendor = Vendor(name)
    vendor_repository.save(vendor)
    return redirect ("/settings")

# SHOW / EDIT
@vendor_blueprint.route("/vendors/<id>")
def show_vendor(id):
    vendor = vendor_repository.select(id)
    transactions = vendor_repository.vendor_transactions(vendor)
    return render_template("vendors/show.html", title="View Vendor", transactions=transactions, vendor=vendor)

# # EDIT
# @vendor_blueprint.route('/vendors/edit/<id>')
# def edit_vendor(id):
#     vendor = vendor_repository.select(id)
#     return render_template("vendors/edit.html", title="Edit Vendor", vendor=vendor)

# UPDATE
@vendor_blueprint.route("/vendors/<id>", methods=['POST'])
def update_vendor(id):
    name = request.form['name']
    if request.form['activate'] == "deactivate":
        active = False
    else:
        active = True
    vendor = Vendor(name, active, id)
    vendor_repository.update(vendor)
    return redirect ("/settings")