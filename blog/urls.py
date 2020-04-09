from django.urls import path, include, re_path
from . import views

app_name = 'blog'
urlpatterns = [
   
    path('', views.post_list, name='post_list'),
    path('show-post/<int:primary_key>/', views.show_post, name='show-post'),
    path('post/new/', views.post_new, name='post-new'),
    path('post/<int:primary_key>/edit/', views.edit_post, name='edit-post'),
    path('drafts/', views.post_draft_list, name='post-draft-list'),
    path('post/<int:pk>/publish', views.post_publish, name='post-publish'),
    path('post/<int:pk>/remove', views.post_remove, name='post-remove')


]
