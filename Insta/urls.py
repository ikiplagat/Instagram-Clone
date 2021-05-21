from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name = 'profile'),
    path('search/', views.search_results, name='search_results')
]