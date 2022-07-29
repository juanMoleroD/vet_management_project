import unittest
from models.vet import Vet

class VetTest(unittest.TestCase):

    def setUp(self):
        self.vet = Vet("Charlie")
    
    def test_vet_has_name(self):
        self.assertEqual("Charlie", self.vet.name)