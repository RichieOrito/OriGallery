from django.db import models

# Create your models here.

class Location(models.Model):
    '''
    Class that defines the lcation of an Image in the gallery
    '''
    name = models.CharField(max_length=30)

    def save_location(self):
        '''
        Method to save the location to the database.
        '''
        self.save()

    def delete_location(self):
        '''
        Method to delete the location from the database.
        '''
        self.delete()

    @classmethod
    def update_location(cls, id, name):
        '''
        Method to update the location in the database.
        '''
        return cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name

class Category(models.Model):
    '''
    Class to define the category of an image on the gallery.
    '''
    name = models.CharField(max_length=30)

    def save_category(self):
        '''
        Method to save the category to the database.
        '''
        self.save()

    def delete_category(self):
        '''
        Method to delete the category from the database.
        '''
        self.delete()

    @classmethod
    def update_category(cls, id, name):
        '''
        Method to update the category in the database.
        '''
        return cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name

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

    def save_image(self):
        '''
        Method to save the image to the database.
        '''
        self.save()

    def delete_image(self):
        '''
        Method to delete the image from the database.
        '''
        self.delete()

    @classmethod
    def update_image(cls, id, image):
        '''Method to update the image in the database.
        '''
        return cls.objects.filter(id=id).update(image=image)
        

    @classmethod
    def get_image_by_id(cls, id):
        '''
        Method to get an image using its ID.
        '''
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_image(cls, search_term):
        '''
        Method to search for an image using its category.
        '''
        try:
            category = Category.objects.get(name__icontains=search_term)
        except Category.DoesNotExist:
            images = []
            return images
        
        return cls.objects.filter(category=category).all()

    @classmethod
    def filter_by_location(cls, location):
        '''Method to filter images by the location.
        '''
        return cls.objects.filter(location=location).all()
    
    def __str__(self):
        return self.name