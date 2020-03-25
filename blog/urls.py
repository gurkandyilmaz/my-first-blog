from django.urls import path, include, re_path
from . import views


urlpatterns = [
   
    path('', views.post_list, name='post_list'),
    path('show-post/<int:primary_key>/', views.show_post, name='show-post'),
]
