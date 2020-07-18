from django.test import TestCase
from .models import *

class ResidentTestClass(TestCase):
    def setUp(self):
        self.cecilia = Resident(first_name='Cecilia', last_name='Barasa', email='ceciheroku@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.cecilia, Resident))

    def test_save_method(self):
        self.cecilia.save_resident()
        residents = Resident.objects.all()
        self.assertTrue(len(residents) > 0)       

