from flask import Flask, Blueprint, render_template, redirect
from repositories import account_repository

account_blueprint = Blueprint("account", __name__)