from django import forms
from .models import Image, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'profile', 'user', 'post_date']
        

class UpdateProfileForm(forms.ModelForm):  
    class Meta:
        model = Profile
        exclude = ['user', 'followers', 'following']
            
     