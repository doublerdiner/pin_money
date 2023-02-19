import datetime

class Goal:
    def __init__(self, savings_target, savings_time_frame, saved_so_far=0, id=None):
        self.savings_target = savings_target
        self.savings_time_frame = datetime.datetime.strptime(savings_time_frame, "%Y-%m-%d")
        self.saved_so_far = saved_so_far
        self.id = id
        self.time_left = []
        
    def time_remaining(self):
        today = datetime.datetime.today()
        time = self.savings_time_frame

        years = time.year - today.year
        months = time.month - today.month
        days = time.day - today.day

        self.time_left = [days, months, years]
        return self.time_left
    
    def goal_comment(self):
        if self.time_left[2] > 0:
            return f"You have {self.time_left[2]} years to meet your goal"
        elif self.time_left[1] > 0:
            return f"You have {self.time_left[1]} months to meet your goal"
        elif self.time_left[0] > 0:
            return f"You have {self.time_left[0]} days to meet your goal"
        else:
            return f"Your goal due date has passed. Please update your goal"
        
    def goal_calculation(self):
        months = (self.time_left[2]*12) + self.time_left[1]
        if months >= 0:
            to_be_saved = (self.savings_target - self.saved_so_far) / months
            to_be_saved = round(to_be_saved, 2)
        return to_be_saved



        
        
        
    # def daily_savings(self):
        # days = self.savings_time_frame - datetime.datetime.today()
        # days = str(days)
        # days = days.split(" ")
        # answer = days[0]
        # if answer < 0:
        #     return "The goal due date has passed."
        # elif answer == 1:
        #     return "You have one day to reach your goal due date."
        
       
