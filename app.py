from flask import Flask, render_template
from controllers.categories_controller import categories_blueprint
from controllers.goals_controller import goals_blueprint
from controllers.transactions_controller import transactions_blueprint
from controllers.vendors_controller import vendors_blueprint
from controllers.settings_controller import settings_blueprint
from controllers.home_controller import home_blueprint

app = Flask(__name__)

app.register_blueprint(categories_blueprint)
app.register_blueprint(goals_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(vendors_blueprint)
app.register_blueprint(settings_blueprint)
app.register_blueprint(home_blueprint)

@app.route('/')
def home():
    return render_template('welcome.html', title = "Welcome")

if __name__ == '__main__':
    app.run(debug=True, port=4999)