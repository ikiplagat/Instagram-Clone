from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.fields import TextField

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
    def update_profile(cls,id,photo,name,bio):
        cls.objects.filter(id=id).update(photo=photo,name=name,bio=bio)              

    @classmethod
    def get_profile_by_id(cls,id):
        profile = cls.objects.get(id=id)
        return profile
    
    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
    
    @classmethod
    def search_profile(cls,username):
        user = User.objects.filter(title__icontains=username)
        return user
    

# Image class.
class Image(models.Model):
    image = CloudinaryField('photo')
    name = models.CharField(max_length =30, blank=True)
    caption = TextField()
    likes = models.IntegerField(blank=True, default=0)
    comments = models.CharField(max_length =2200, blank=True)
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
    
    def save_comment(self):
        self.save()
        
    def delete_comment(self):
        self.delete()      

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments