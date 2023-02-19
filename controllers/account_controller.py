from flask import Flask, Blueprint, render_template, redirect
from repositories import account_repository
from models.account import Account

account_blueprint = Blueprint("account", __name__)

# INDEX
# GET '/account'

