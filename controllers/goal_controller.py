from flask import Flask, Blueprint, render_template, redirect
from repositories import goal_repository

goal_blueprint = Blueprint("goal", __name__)