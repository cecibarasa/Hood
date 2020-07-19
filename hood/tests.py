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

    def test_update_hood(self):
        self.the_hood.save_hood()
        self.the_hood.update_hood(self.the_hood.id,'maldives')
        update = Hood.objects.get(name = "maldives")
        self.assertEqual(update.name, 'maldives')

    def test_update_residents(self):
        self.the_hood.save_resident()
        self.the_hood.update_residents(self.the_hood.id,'maldives')
        update = Hood.objects.get(name = "maldives")
        self.assertEqual(update.name, 'maldives')        

class ProfileTestCLass(TestCase):
    '''
    setup self instance of profile
    '''

    def setUp(self):
        self.the_hood = Hood(name='kasa',location_name='kasarani',residents=5)
        self.the_hood.save_hood()

        self.new_user = User(username='cecilia')
        self.new_user.save()

        self.new_profile = Profile(bio='Tired', full_names='Cecilia Barasa', profile_picture='img.jpg', hood=self.the_hood,user=self.new_user)
        self.new_profile.save()

    ''' 
    test instance of profile
    '''

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="jazz",email="jazz@gmail.com")
        self.new_user.save()
        self.the_hood = Hood(name='kasa', location_name='kasarani', residents=5)
        self.the_hood.save()
        self.burgers = Business(business_name='jazz-burgers',address='ceciliam@gmail.com',owner=self.new_user,hood=self.the_hood)
        self.burgers.save()

    def tearDown(self):
        User.objects.all().delete()
        Hood.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.burgers,Business))

    def test_save_business(self):
        self.burgers.create_business()
        business =  Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_update_business(self):
        self.burgers.save_business()
        self.burgers.update_business(self.burgers.id,'maldives')
        update = Business.objects.get(business_name = "maldives")
        self.assertEqual(update.business_name, 'maldives')            

class PostTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username="jazz", email="jazz@gmail.com")
        self.new_user.save()
        self.the_hood = Hood(name='kasa', location_name='kasarani', residents=5)
        self.the_hood.save()

        self.new_post=Post(title = 'Robbed',description = 'I was robbed')

    def tearDown(self):
        User.objects.all().delete()
        Hood.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))                            