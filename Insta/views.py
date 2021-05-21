from django.shortcuts import render
from django.http  import HttpResponse
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
import datetime as dt
from django.contrib.auth.models import User

# Create your views here.
# Feed
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    
    return render(request, 'post/index.html', { "images": images})

# Profile page
@login_required(login_url='/accounts/login/')
def profile(request):
    date = dt.date.today()
    # profile = Profile.objects.filter(id = profile_id)
    images = Image.objects.filter(user = request.user)
    
    return render(request, 'profile/profile.html', {"date": date, "images": images, })