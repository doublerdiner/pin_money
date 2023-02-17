from datetime import datetime

class Goal:
    def __init__(self, monthly_take_home_pay, savings_target, savings_time_frame=None, id=None):
        self.monthly_take_home_pay = monthly_take_home_pay
        self.savings_target = savings_target
        self.savings_time_frame = datetime.strptime(savings_time_frame, "%d %m %Y")
        self.id = id
        