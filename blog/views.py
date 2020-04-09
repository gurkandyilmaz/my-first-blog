from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

from django.contrib.auth.decorators import login_required


from .models import Post, Comment
from .forms import PostForm, CommentForm
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
			return redirect('blog:show-post', primary_key=post.pk)
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
			return redirect('blog:show-post', primary_key=post.pk)
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
	return redirect('blog:show-post', primary_key=pk)

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()

	return redirect('blog:post_list' )


@login_required
def add_comment(request, primary_key):
	post = get_object_or_404(Post, pk=primary_key)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('blog:show-post', primary_key=post.pk)
	else:
		form = CommentForm()


	return render(request, 'blog/add_comment.html', {'form':form})

@login_required
def comment_remove(request, pk_comment):
	
	comment = get_object_or_404(Comment, pk=pk_comment)
	pk = comment.post_id
	comment.delete()

	return redirect('blog:show-post', primary_key=pk)

@login_required
def comment_approve(request, pk_comment):
	comment = get_object_or_404(Comment, pk=pk_comment)
	comment.approve()

	return redirect('blog:show-post', primary_key=comment.post.pk)

