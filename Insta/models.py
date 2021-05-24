from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.fields import TextField

# Create your models here.

# Profile class.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = CloudinaryField('photo', blank=True)
    name =  models.CharField(max_length =30, blank=True)
    bio = models.CharField(max_length =150, blank=True)
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
    def get_profile(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile
    
    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
    
    @classmethod
    def get_user(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile
  
    

# Image class.
class Image(models.Model):
    image = CloudinaryField('photo')
    name = models.CharField(max_length =30, blank=True)
    caption = TextField()
    likes=models.ManyToManyField(Profile,related_name="posts")
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
        
    def likes_num(self):
        self.likes.count()    
        
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images 
    
    @classmethod
    def get_image_by_user(cls,username):
        images = cls.objects.filter(user__username__contains=username)
        return images     
    
    
class Follow(models.Model):
  posted = models.DateTimeField(auto_now_add=True)
  followed = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="profile_followed")
  follower = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="profile_follower")

  def __str__(self):
    return self.pk
         


class Comment(models.Model):
    comment = models.TextField(max_length=2200)
    user = models.ForeignKey(User, related_name='commented_by', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='comment_for', on_delete=models.CASCADE)
    pub_date=models.DateField(auto_now_add=True)

    def __str__(self):  
        return self.comment
    
    def save_comment(self):
        self.save()
        
    def delete_comment(self):
        self.delete()      

    @classmethod
    def get_comments(cls,image):
        return cls.objects.filter(image=image)

    
    class Meta:
        ordering=['-pub_date']