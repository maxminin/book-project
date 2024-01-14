from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request,
                  'post-list.html',
                  {'posts' : posts})
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.all()    #related name
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', pk=pk)   #pk=pk для маршрутизации в urls
    else:
        form = CommentForm()
    return render(request,
                  'post-detail.html',
                  {'post' : post,
                   'comments': comments,
                   'form': form})
@csrf_exempt
def post_create(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = AddPostForm()
    return render (request,
            'post-create.html',
            {'form': form})
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request,
                  'post_delete.html',
                  {'post' : post})




