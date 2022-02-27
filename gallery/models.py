from django.db import models

# Create your models here.

class Location(models.Model):
    '''
    Class that defines the lcation of an Image in the gallery
    '''
    name = models.CharField(max_length=30)

class Category(models.Model):
    '''
    Class to define the category of an image on the gallery.
    '''
    name = models.CharField(max_length=30)

class Image(models.Model):
    '''
    Class to define attributes of an image in the gallery and it's methods.
    '''

    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    post_date = models.DateField(auto_now_add=True)