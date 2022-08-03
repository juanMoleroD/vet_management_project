from datetime import datetime
import unittest

from models.animal import Animal
from models.vet import Vet
from models.owner import Owner

class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("Charlie")
        self.owner = Owner("Juan", "07007707707")
        self.animal = Animal("Mandy", datetime(2019,7,9), "dog", self.owner, self.vet )
    
    def test_animal_has_name(self):
        self.assertEqual("Mandy", self.animal.name)
    
    def test_animal_has_DOB(self):
        self.assertEqual( datetime(2019,7,9), self.animal.date_of_birth)
    
    def test_animal_has_type(self):
        self.assertEqual("dog", self.animal.type)

    def test_animal_has_contact_details(self):
        self.assertEqual("07007707707", self.animal.get_contact_details())