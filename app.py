from flask import Flask, render_template
from controllers.category_controller import category_blueprint
from controllers.goal_controller import goal_blueprint
from controllers.transaction_controller import transaction_blueprint
from controllers.vendor_controller import vendor_blueprint
from controllers.account_controller import account_blueprint

app = Flask(__name__)

app.register_blueprint(category_blueprint)
app.register_blueprint(goal_blueprint)
app.register_blueprint(transaction_blueprint)
app.register_blueprint(vendor_blueprint)
app.register_blueprint(account_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title = "Home")

if __name__ == '__main__':
    app.run(debug=True, port=4999)