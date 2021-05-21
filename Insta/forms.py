from django import forms
from .models import Image

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'profile', 'user', 'post_date']
     