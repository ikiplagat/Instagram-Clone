from django.shortcuts import render
from django.http  import HttpResponse
from .email import send_welcome_email

# Create your views here.
def index(request):
    return render(request, 'index.html')