from django.urls import path, re_path
from django.urls.conf import include
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name = 'profile'),
    path('explore/', views.explore, name='explore'),
    path('search/', views.search_results, name='search_results'),
    re_path(r'^post/(\d+)',views.single_post,name ='single_post'),
    path('tinymce/', include('tinymce.urls')),
    path('new/post', views.new_post, name='new_post')
]