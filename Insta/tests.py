from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile, Image, Comment

# Create your tests here.

# Profile class tests
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User()
        self.user.save()
        self.profile = Profile(user = self.user, photo = 'img', name = 'img', bio = 'I am Levlest', followers = 0, following = 0)
      
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
        self.user = User()
        self.user.save()
        self.profile= Profile(user = self.user, photo = 'img', name = 'img', bio = 'I am Levlest', followers = 0, following = 0)
        self.profile.save()
        self.image = Image(image = 'img', name = 'Kasparov', caption = 'I am Levlest', likes = 0, comments = 'Wowz', profile = self.profile, user = self.user, post_date = '')
      
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
        
        
class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User()
        self.user.save()
        self.profile= Profile(user = self.user, photo = 'img', name = 'img', bio = 'I am Levlest', followers = 0, following = 0)
        self.profile.save()
        self.image = Image(image = 'img', name = 'Kasparov', caption = 'I am Levlest', likes = 0, comments = 'Wowz', profile = self.profile, user = self.user, post_date = '')
        self.image.save()
        self.comment = Comment(content = 'This is lovely', user = self.user, image = self.image)
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))        
        
    # Testing Save Method
    def test_save_method(self):  
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)    
        
    def tearDown(self):
        User.objects.all().delete() 
        Profile.objects.all().delete()        
        Image.objects.all().delete() 
        Comment.objects.all().delete() 
        
    def test_delete_comment(self):
        self.comment.save_comment()
        comments=Comment.objects.all()
        self.assertEqual(len(comments),1)
        self.comment.delete_comment()
        del_comments=Comment.objects.all()
        self.assertEqual(len(del_comments),0)      