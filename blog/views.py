from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.


def post_list(request):
	posts = Post.objects.all().order_by('published_date')
	content_dict = {'all_posts':posts}

	return render(request, 'blog/post_list.html', context=content_dict)