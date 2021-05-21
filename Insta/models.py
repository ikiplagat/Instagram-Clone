from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

# Profile class.
class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile' ,on_delete=models.CASCADE)
    photo = CloudinaryField('photo')
    name =  models.CharField(max_length =30)
    bio = models.CharField(max_length =150)
    followers=models.IntegerField(default=0)
    following=models.IntegerField(default=0)
  
    def __str__(self):
        return self.user.username
        
    def save_profile(self):
        self.save()
          
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def update_profile(cls,id,bio):
        cls.objects.filter(id=id).update(bio=bio)              

    @classmethod
    def get_profile_by_id(cls,id):
        profile = cls.objects.get(id=id)
        return profile
    
    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
    
    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(user=search_term)
        return profile
    

# Image class.
from tinymce.models import HTMLField
class Image(models.Model):
    image = CloudinaryField('photo')
    name = models.CharField(max_length =30)
    caption = HTMLField()
    likes = models.IntegerField(null=True)
    comments = models.CharField(max_length =2200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-post_date']
    
    def __str__(self):
        return self.name
        
    def save_image(self):
        self.save()  
          
    def delete_image(self):
        self.delete()  
        
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images            


class Comment(models.Model):
    content = models.TextField(max_length=150)
    user = models.ForeignKey(User, related_name='commented_by', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='comment_for', on_delete=models.CASCADE)

    def __str__(self):  
        return self.content

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments