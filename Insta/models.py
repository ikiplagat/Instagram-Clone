from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
  photo = CloudinaryField('photo')
  bio = models.CharField(max_length =150)

class Image(models.Model):
  image = CloudinaryField('photo')
  name = models.CharField(max_length =30)
  caption = models.TextField(max_length =2200)
  likes = models.IntegerField()
  comments = models.CharField
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
