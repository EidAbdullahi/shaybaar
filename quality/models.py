from django.db import models
import datetime as dt


from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video


# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=60)

    def __str__(self):
        '''
        A string representation
        '''
        return self.location_name

    def save_location(self):
        '''
        A method that saves the location name
        '''
        return self.save()

    @classmethod
    def delete_location(cls, id):
        return cls.objects.filter(id = id).delete()


class category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        '''
        String representation
        '''
        return self.category_name

    def save_category(self):
        '''
        Method to save the category name
        '''
        return self.save()


class Image(models.Model):
    '''
    A class that determines the image model characteristics
    '''
    image_name = models.CharField(max_length=30)
    image_desc = models.TextField()
    photo = CloudinaryField('image')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ManyToManyField(category)
    post_date = models.DateTimeField(auto_now_add=True)
    # photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        '''
        String representation
        '''
        return self.image_name

    def save_photo(self):
        '''
        A method that saves photo
        '''
        return self.save()

    @classmethod
    def show_all_photos(cls):
        '''
        A method that returns all photos posted in order of the most recent
        '''
        return cls.objects.order_by("post_date")[::-1]

    @classmethod
    def delete_photo(cls, id):
        '''
        A method that deletes a photo
        '''
        return cls.objects.filter(id = id).delete()

    @classmethod
    def get_photo_by_id(cls, id):
        '''
        A method to get a photo bases on the id
        '''
        return cls.objects.filter(id = id).all()

    @classmethod
    def search_photo_by_category(cls, category):
        '''
        A method to return all photos that are a specific category
        '''
        gallery = cls.objects.filter(category__category_name__icontains = category)
        return gallery

    @classmethod
    def filter_by_location(cls, search_term):
        '''
        A method to filter all photos based on a location
        '''
        locations = cls.objects.filter(location__location_name__icontains=search_term)
        return locations


class jobs(models.Model):
    '''
    A class that determines the image model characteristics
    '''
    title = models.CharField(max_length=30)
    role = models.TextField()
    desc= models.TextField()
    salary=models.CharField(max_length=30)
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''
        String representation
        '''
        return self.title

    def save_job(self):
        '''
        A method that saves jobs
        '''
        return self.save()    


class Contact(models.Model):
    '''
    A class that determines the image model characteristics
    '''
    name = models.CharField(max_length=30)
    email =models.EmailField(max_length=254)
    contact= models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    comment=models.TextField()
    
    
    def __str__(self):
        '''
        String representation
        '''
        return self.name

    def save_Contact(self):
        '''
        A method that saves contact
        '''
        return self.save()       


class Video(models.Model):
    caption=models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/', blank=True, storage=VideoMediaCloudinaryStorage(),
                              validators=[validate_video])
    


    def __str__(self):
        return self.caption

    def save_Video(self):
        '''
        A method that saves contact
        '''
        return self.save()       
    


class Application(models.Model):
    '''
    A class that determines the image model characteristics
    '''
    name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    email =models.EmailField(max_length=254)
    contact= models.IntegerField()
    qualifications=models.TextField()
    cv= models.FileField()
    
    
    def __str__(self):
        '''
        String representation
        '''
        return self.name

    def save_Application(self):
        '''
        A method that saves application
        '''
        return self.save()                      
