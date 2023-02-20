from flask import Flask, Blueprint, render_template, redirect, request
import datetime
from repositories import goal_repository
from models.goal import Goal

goal_blueprint = Blueprint("goal", __name__)

# INDEX

@goal_blueprint.route('/goals')
def goals():
    # Date
    today = datetime.datetime.now()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    # transactions
    goals = goal_repository.select_all()
       
    return render_template("goals/index.html", title="Goals", month=month, year=year, goals=goals)

# NEW

@goal_blueprint.route('/goals/new')
def new_goal():
    today = datetime.datetime.now()
    return render_template('goals/new.html', today=today)

# CREATE

@goal_blueprint.route('/goals', methods=['POST'])
def create_goal():
    name = request.form['name']
    savings_target = request.form['savings_target']
    savings_time_frame = request.form['savings_time_frame']
    saved_so_far = request.form['saved_so_far']
    goal = Goal(name, savings_target, savings_time_frame, saved_so_far)
    goal_repository.save(goal)
    return redirect ("/goals")

# SHOW

@goal_blueprint.route("/goals/<id>")
def show_goal(id):
    goal = goal_repository.select(id)
    return render_template("goals/show.html", goal=goal)

# EDIT

@goal_blueprint.route('/goals/edit/<id>')
def edit_goal(id):
    goal = goal_repository.select(id)
    return render_template("goals/edit.html", goal=goal)

# UPDATE

@goal_blueprint.route("/goals/<id>", methods=['POST'])
def update_goal(id):
    name = request.form['name']
    savings_target = request.form['savings_target']
    savings_time_frame = request.form['savings_time_frame']
    saved_so_far = request.form['saved_so_far']
    goal = Goal(name, savings_target, savings_time_frame, saved_so_far, id)
    goal_repository.update(goal)
    return redirect ("/goals")

# DELETE

@goal_blueprint.route("/goals/delete/<id>", methods=['POST'])
def delete_goal(id):
    goal_repository.delete(id)
    return redirect("/goals")