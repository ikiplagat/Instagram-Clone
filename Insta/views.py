from django.shortcuts import render
from django.http  import HttpResponse
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')