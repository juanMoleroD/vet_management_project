from datetime import datetime

class Appointment:
    def __init__(self, animal, check_in, check_out, id = None):
        self.animal = animal
        self.check_in = check_in
        self.check_out = check_out
        self.id = id

    def get_formated_date(self, datetime_obj):
        return datetime.strftime(datetime_obj, "%Y-%m-%d")