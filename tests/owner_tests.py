import unittest
from models.owner import Owner

class OwnerTest(unittest.TestCase):
    def setUp(self):
        self.owner_with_no_animals = Owner("Juan", "07007707707", [])
    
    def test_owner_has_name(self):
        self.assertEqual("Juan", self.owner_with_no_animals.name)
    
    def test_owner_has_contact_details(self):
        self.assertEqual("07007707707", self.owner_with_no_animals.contact_details)

    def test_owner_can_have_no_animals(self):
        self.assertFalse(self.owner_with_no_animals.animals)