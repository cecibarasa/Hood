from django.test import TestCase
from .models import *

class ResidentTestClass(TestCase):
    def setUp(self):
        self.cecilia = Resident(first_name = 'Cecilia', last_name= 'Barasa', email = 'ceciheroku@gmail.com')

