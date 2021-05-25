from django import forms
from .models import Image, Profile, Follow

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'profile', 'user', 'post_date']
        

class UpdateProfileForm(forms.ModelForm):  
    class Meta:
        model = Profile
        exclude = ['user', 'followers', 'following']
        
        
class FollowForm(forms.ModelForm):
  class Meta:
    model = Follow
    exclude = ['followed','follower']

class UnfollowForm(forms.ModelForm):
  class Meta:
    model = Follow
    exclude = ['followed','follower']        
            
     