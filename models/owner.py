class Owner:
    def __init__(self, name, contact_details, registered = True, id = None):
        self.name = name
        self.contact_details = contact_details
        self.registered = registered
        self.id = id

    def unregister(self):
        self.registered = False
    
    def reregister(self):
        self.registered = True