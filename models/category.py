class Category:
    def __init__(self, name, active=True, id=None):
        self.name = name
        self.active = active
        self.id = id  

    def category_change_active_status(self):
        if self.active:
            self.active = False
        else:
            self.active = True