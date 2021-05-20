from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# Profile class.
class Profile(models.Model):
    photo = CloudinaryField('photo')
    bio = models.CharField(max_length =150)
  
    def __str__(self):
        return self.bio
        
    def save_profile(self):
        self.save()
          
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def update_profile(cls,id,bio):
        cls.objects.filter(id=id).update(bio=bio)              


# Image class.
class Image(models.Model):
    image = CloudinaryField('photo')
    name = models.CharField(max_length =30)
    caption = models.TextField(max_length =2200)
    likes = models.IntegerField()
    comments = models.CharField(max_length =2200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
    def save_image(self):
        self.save()  
          
    def delete_image(self):
        self.delete()          
