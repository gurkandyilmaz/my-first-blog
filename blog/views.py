from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

from django.contrib.auth.decorators import login_required


from .models import Post
from .forms import PostForm
# Create your views here.


def post_list(request):
	posts = Post.objects.all().order_by('-published_date')
	content_dict = {'all_posts':posts}

	return render(request, 'blog/post_list.html', context=content_dict)

def show_post(request, primary_key):
	post = get_object_or_404(Post, pk=primary_key)


	return render(request, 'blog/show_post.html', {'single_post':post})

@login_required
def post_new(request):
	if request.method == 'POST': 
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user

			post.save()
			return redirect('show-post', primary_key=post.pk)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def edit_post(request, primary_key):
	post = get_object_or_404(Post, pk=primary_key)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user

			post.save()
			return redirect('show-post', primary_key=post.pk)
	else:
		form = PostForm(instance=post)
		
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')


	return render(request, 'blog/post_draft_list.html', {'posts':posts})  

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('show-post', primary_key=pk)

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()

	return redirect('post_list' )
