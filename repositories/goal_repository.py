from db.run_sql import run_sql

from models.goal import Goal

# This repository was tested on 19/02/23.
# All passed

def save(goal):
    sql = "INSERT INTO goals (name, savings_target, savings_time_frame, saved_so_far) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [goal.name, goal.savings_target, goal.savings_time_frame, goal.saved_so_far]
    results = run_sql(sql, values)
    id = results[0]['id']
    goal.id = id
    return goal

def select_all():
    goals = []
    sql = "SELECT * FROM goals ORDER BY savings_time_frame ASC"
    results = run_sql(sql)
    for row in results:
        goal = Goal(row['name'], row['savings_target'], row['savings_time_frame'], row['saved_so_far'], row['id'])
        goals.append(goal)
    return goals

def select(id):
    goal = None
    sql = "SELECT * FROM goals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        goal = Goal(result['name'], result['savings_target'], result['savings_time_frame'], result['saved_so_far'], result['id'])
    return goal

def delete(id):
    sql = "DELETE FROM goals WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM goals"
    run_sql(sql)

def update(goal):
    sql = "UPDATE goals SET (name, savings_target, savings_time_frame, saved_so_far) = (%s, %s, %s, %s) WHERE id = %s"
    values = [goal.name, goal.savings_target, goal.savings_time_frame, goal.saved_so_far, goal.id]
    run_sql(sql, values)

# def select_newest():
    
    

    