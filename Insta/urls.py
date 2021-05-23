from django.urls import path, re_path
from django.urls.conf import include
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name = 'profile'),
    path('explore/', views.explore, name='explore'),
    path('search/', views.search, name='search_results'),
    re_path('post/(?P<image_id>\d+)',views.single_post,name ='single_post'),
    path('tinymce/', include('tinymce.urls')),
    path('new/post', views.new_post, name='new_post'),
    path('update_profile', views.update_profile, name='update_profile')
]