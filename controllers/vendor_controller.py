from flask import Flask, Blueprint, render_template, redirect, request
from repositories import vendor_repository
from models.vendor import Vendor

vendor_blueprint = Blueprint("vendor", __name__)

# NEW
@vendor_blueprint.route('/vendors/new')
def new_vendor():
    return render_template('vendors/new.html') 

# CREATE
@vendor_blueprint.route('/vendors', methods=['POST'])
def create_vendor():
    name = request.form['name']
    vendor = Vendor(name)
    vendor_repository.save(vendor)
    return redirect ("/settings")

# EDIT
@vendor_blueprint.route('/vendors/edit/<id>')
def edit_vendor(id):
    vendor = vendor_repository.select(id)
    return render_template("vendors/edit.html", vendor=vendor)

# UPDATE
@vendor_blueprint.route("/vendors/<id>", methods=['POST'])
def update_vendor(id):
    name = request.form['name']
    if request.form['deactivates'] == "deactivate":
        deactivated = True
    else:
        deactivated = False
    vendor = Vendor(name, deactivated, id)
    vendor_repository.update(vendor)
    return redirect ("/settings")