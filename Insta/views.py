from django.shortcuts import render, redirect
from django.http  import Http404
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Profile, Image, Comment
import datetime as dt
from django.contrib.auth.models import User
from .forms import NewPostForm, UpdateProfileForm

# Create your views here.
# Feed
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    comments = Comment.objects.all()
    
    return render(request, 'post/index.html', { "images": images, "comments": comments})

# Explore
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

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'post/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'post/search.html',{"message":message})
    
@login_required(login_url='/accounts/login/')
def single_post(request,image_id):
    try:
        single_post= Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"post/single_post.html", {"single_post":single_post})    

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'post/new_post.html', {"form": form})

# Update profile
@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = UpdateProfileForm()
    return render(request, 'profile/profile_edit.html', {"form": form})

# @login_required(login_url='/accounts/login/')
# def add_comment(request);