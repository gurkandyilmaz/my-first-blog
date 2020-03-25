from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post
# Create your views here.


def post_list(request):
	posts = Post.objects.all().order_by('published_date')
	content_dict = {'all_posts':posts}

	return render(request, 'blog/post_list.html', context=content_dict)

def show_post(request, primary_key):
	post = get_object_or_404(Post, pk=primary_key)


	return render(request, 'blog/show_post.html', {'single_post':post})