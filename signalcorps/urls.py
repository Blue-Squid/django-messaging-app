from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    path('index/', views.index, name ='index'),
    url(r'^index/profile/$', views.profile, name='profile'),
    url(r'^index/viewPosts/$', views.view_message, name='viewPosts'),
    url(r'^logout/$', views.log_out, name = 'logout'),
]