from datetime import datetime

class Transaction:
    def __init__(self, name, cost, date, monthly_recurring=False, notes=None, id=None):
        self.name = name
        self.cost = cost
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.monthly_recurring = monthly_recurring
        self.notes = notes
        self.id = id

    def change_monthly_recurring(self):
        if self.monthly_recurring:
            self.monthly_recurring = False
        else:
            self.monthly_recurring = True