class Category:
    def __init__(self, name, transaction, deactivated=False, id=None):
        self.name = name
        self.transaction = transaction 
        self.deactivated = deactivated
        self.id = id

    def change_deactivated_status(self):
        if self.deactivated:
            self.deactivated = False
        else:
            self.deactivated = True