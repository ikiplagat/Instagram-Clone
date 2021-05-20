from django.test import TestCase
from .models import Profile, Image

# Create your tests here.

# Profile class tests
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.profile = Profile(photo = 'img', bio = 'I am Levlest')
      
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    # Testing Save Method
    def test_save_method(self):  
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
    def tearDown(self):
        Profile.objects.all().delete()
      
    def delete_profile(self):
        self.delete() 
        
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.id,'I am Levlest')
        update=Profile.objects.get(bio='I am Levlest')
        self.assertEqual(update.bio,'I am Levlest')                      
        
        
# Image class tests
class ImageTestClass(TestCase):
  # Set up method
    def setUp(self):
        self.profile= Profile(photo = 'img', bio = 'I am Levlest')
        self.profile.save()
        self.image = Image(image = 'img', name = 'Kasparov', caption = 'I am Levlest', likes = 0, comments = 'Wowz', profile = self.profile)
      
  # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))        

    # Testing Save Method
    def test_save_method(self):  
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
    def tearDown(self):
        Image.objects.all().delete() 
        Profile.objects.all().delete()    
      
    def test_delete_image(self):
        self.image.save_image()
        images=Image.objects.all()
        self.assertEqual(len(images),1)
        self.image.delete_image()
        del_images=Image.objects.all()
        self.assertEqual(len(del_images),0)      