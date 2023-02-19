class Vendor:
    def __init__(self, name, deactivated=False, id=None):
        self.name = name
        self.deactivated = deactivated
        self.id = id

    def vendor_change_deactivated_status(self):
        if self.deactivated:
            self.deactivated = False
        else:
            self.deactivated = True