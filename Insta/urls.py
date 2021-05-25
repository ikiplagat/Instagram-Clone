from django.urls import path, re_path
from django.urls.conf import include
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/<username>',views.profile,name='profile'),
    path('explore/', views.explore, name='explore'),
    path('search/', views.search, name='search_results'),
    re_path('post/(?P<image_id>\d+)',views.single_post,name ='single_post'),
    re_path('like/(?P<image_id>\d+)',views.like_post,name='likePost'),
    re_path('comment/(?P<image_id>\d+)',views.comment,name='addComment'),
    path('tinymce/', include('tinymce.urls')),
    path('new/post', views.new_post, name='new_post'),
    path('create_profile/', views.update_profile, name='update_profile'),
    path('welcome/', views.welcome_mail, name='welcome_email'),
]