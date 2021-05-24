from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http  import Http404, HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Profile, Image, Comment
import datetime as dt
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import NewPostForm, UpdateProfileForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    '''
    Timeline
    '''
    images = Image.objects.all()
    comments = Comment.objects.all()
    
    return render(request, 'post/index.html', { "images": images, "comments": comments})

# Explore
@login_required(login_url='/accounts/login/')
def explore(request):
    '''
    Explore various user posts
    '''
    images = Image.objects.all()
    
    return render(request, 'post/explore.html', { "images": images})

# Profile page
@login_required(login_url='/accounts/login/')
def profile(request, username):
    '''
    Method to display a specific user profile
    '''
    date = dt.date.today()
    images = Image.get_image_by_user(username)
    profile = Profile.get_user(username)
    # try:
    #     profile = Profile.get_user(username)
    # except ObjectDoesNotExist:
    #     raise Http404()
    
    return render(request, 'profile/profile.html', {"date": date, "images": images, "profile": profile })

@login_required(login_url='/accounts/login/')
def search(request):
    '''
    Method to search for a specific user using the user profile
    '''
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_profiles = Profile.get_profile(search_term)
        print(searched_profiles)
        message = f"{search_term}"

        return render(request, 'post/search.html',{"message":message, "profiles": searched_profiles})

    else:
        message = "You haven't searched for any item"
        return render(request, 'post/search.html',{"message":message})
    
@login_required(login_url='/accounts/login/')
def single_post(request,image_id):
    '''
    Method to display a single post
    '''
    try:
        single_post= Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"post/single_post.html", {"single_post":single_post})    

@login_required(login_url='/accounts/login/')
def new_post(request):
    '''
    Method to create a post
    '''
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
    '''
    Method to update a user profile
    '''
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile', username=current_user.username)

    else:
        form = UpdateProfileForm()
    return render(request, 'profile/profile_edit.html', {"form": form})

@login_required(login_url='/accounts/login/')
def comment(request,image_id):
    '''
    Method to add post comments
    '''
    image=Image.objects.get(pk=image_id)
    comments=request.GET.get("comments")
    current_user=request.user
    comment=Comment(image=image,comment=comments,user=current_user)
    comment.save_comment()

    return redirect('index')

@login_required(login_url='/accounts/login/')
def like_post(request,image_id):
    '''
    Method to like a post
    '''
    image = Image.objects.get(pk=image_id)
    is_liked=False
    user=request.user
    try:
        profile=Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        raise Http404()
    if image.likes.filter(id=profile.id).exists():
        image.likes.remove(profile)
        is_liked=False
    else:
        image.likes.add(profile)
        is_liked=True
    return HttpResponseRedirect(reverse('index'))