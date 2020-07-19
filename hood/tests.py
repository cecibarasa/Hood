from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class ResidentTestClass(TestCase):
    def setUp(self):
        self.cecilia = Resident(first_name='Cecilia', last_name='Barasa', email='ceciheroku@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.cecilia, Resident))

    def test_save_method(self):
        self.cecilia.save_resident()
        residents = Resident.objects.all()
        self.assertTrue(len(residents) > 0)       

class HoodTestClass(TestCase):
    def setUp(self):
        self.the_hood =Hood(name='kasa',location_name='kasarani',residents=5)
        self.the_hood.save()

    def tearDown(self):
        Hood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.the_hood,Hood))

    def test_save_hood(self):
        self.the_hood.save_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)