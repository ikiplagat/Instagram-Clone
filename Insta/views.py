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

# Feed
@login_required(login_url='/accounts/login/')
def explore(request):
    images = Image.objects.all()
    
    return render(request, 'post/explore.html', { "images": images})

# Profile page
@login_required(login_url='/accounts/login/')
def profile(request):
    date = dt.date.today()
    # profile = Profile.objects.filter(id = profile_id)
    images = Image.objects.filter(user = request.user)
    
    return render(request, 'profile/profile.html', {"date": date, "images": images, })

# Update profile
@login_required(login_url='/accounts/login/')
def profile_update(request):
    
    return render(request, 'profile/profile_edit')

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'post/explore.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'post/explore.html',{"message":message})