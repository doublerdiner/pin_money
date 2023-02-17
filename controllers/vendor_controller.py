from flask import Flask, Blueprint, render_template, redirect
from repositories import vendor_repository

vendor_blueprint = Blueprint("vendor", __name__)