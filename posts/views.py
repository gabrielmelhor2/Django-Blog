from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import *
from django.db.models import Q

def posts_view(request):
    query = request.GET.get('search', None)
    
    if query and len(query) > 1:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        if query:
            posts = Post.objects.none()
        else: 
            posts = Post.objects.all()

    return render(request, "posts.html", {'posts': posts})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(('posts_view'))
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})
    
    