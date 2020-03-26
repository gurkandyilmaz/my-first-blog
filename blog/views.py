from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone


from .models import Post
from .forms import PostForm
# Create your views here.


def post_list(request):
	posts = Post.objects.all().order_by('published_date')
	content_dict = {'all_posts':posts}

	return render(request, 'blog/post_list.html', context=content_dict)

def show_post(request, primary_key):
	post = get_object_or_404(Post, pk=primary_key)


	return render(request, 'blog/show_post.html', {'single_post':post})


def post_new(request):
	if request.method == 'POST': 
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('show-post', primary_key=post.pk)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form':form})


def edit_post(request, primary_key):
	post = get_object_or_404(Post, pk=primary_key)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('show-post', primary_key=post.pk)
	else:
		form = PostForm(instance=post)
		
	return render(request, 'blog/post_edit.html', {'form':form})


