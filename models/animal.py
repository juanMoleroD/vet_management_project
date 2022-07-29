from datetime import date


class Animal:
    def __init__(self, name, date_of_birth, type, owner, vet, treatment_notes, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.type = type
        self.owner = owner
        self.vet = vet
        self.treatment_notes = treatment_notes
        self.id = id