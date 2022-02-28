from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.

class LocationTest(TestCase):
    def setUp(self):
        self.test_location = Location(name='Nanyuki')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_location, Location))

    def test_save_location(self):
        self.test_location.save_location()
        self.assertTrue(len(Location.objects.all()) > 0)

    def test_delete_location(self):
        self.test_location.save_location()
        self.assertTrue(len(Location.objects.all()) > 0)
        self.test_location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

    def test_update_location(self):
        self.test_location.save_location()
        self.test_location.update_location(self.test_location.id, 'Nairobi')
        self.assertTrue(Location.objects.get(name='Nairobi').name, 'Nairobi')
        self.assertTrue(len(Location.objects.all())==1)

class CategoryTest(TestCase):
    def setUp(self):
        self.test_category = Category(name='beaches')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_category, Category))

    def test_save_category(self):
        self.test_category.save_category()   
        self.assertTrue(len(Category.objects.all()) > 0)

    def test_delete_category(self):     
        self.test_category.save_category()
        self.assertTrue(len(Category.objects.all()) > 0)
        self.test_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)

    def test_update_category(self):
        self.test_category.save_category()
        self.test_category.update_category(self.test_category.id, 'wildlife')
        self.assertTrue(Category.objects.get(name='wildlife').name, 'wildlife')
        self.assertTrue(len(Category.objects.all())==1)

class ImageTest(TestCase):
    '''
       Class to test the Image class.
    '''

    def setUp(self):
        self.mombasa = Location(name='kakamega')
        self.mombasa.save_location()

        self.travel = Category(name='vegetation')
        self.travel.save_category()

        self.hiking_image=Image(name='Forest',description='being apart of Nature is a beautiful thing',location=self.mombasa,category=self.travel)

