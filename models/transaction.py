from datetime import datetime

class Transaction:
    def __init__(self, name, cost, date, category, vendor, monthly_recurring=False, notes=None, id=None):
        self.name = name
        self.cost = cost
        self.date = date
        self.category = category
        self.vendor = vendor
        self.monthly_recurring = monthly_recurring
        self.notes = notes
        self.id = id

    def change_monthly_recurring(self):
        if self.monthly_recurring:
            self.monthly_recurring = False
        else:
            self.monthly_recurring = True

    def obtain_month_int(self):
        date = datetime.strftime(self.date, "%Y-%m-%d")
        string = date.split("-")
        month = string[1]
        return int(month)
